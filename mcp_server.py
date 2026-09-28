import sys
import json
from client import PedersenCommitment

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "pedersen_commit",
                        "description": "Create Pedersen commitment or verify homomorphic sum",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "action": {"type": "string", "enum": ["commit", "verify", "add"]},
                                "val": {"type": "integer"},
                                "blinding": {"type": "integer"},
                                "commitment": {"type": "integer"},
                                "c1": {"type": "integer"},
                                "c2": {"type": "integer"}
                            },
                            "required": ["action"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "pedersen_commit":
            act = args["action"]
            if act == "commit":
                c = PedersenCommitment.commit(args["val"], args["blinding"])
                return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"commitment": c})}]}}
            elif act == "verify":
                ok = PedersenCommitment.verify(args["commitment"], args["val"], args["blinding"])
                return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"verified": ok})}]}}
            elif act == "add":
                c_sum = PedersenCommitment.add_commitments(args["c1"], args["c2"])
                return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"sum_commitment": c_sum})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
