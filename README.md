# Pedersen Commitment Scheme Skill

High-efficiency, zero-dependency Python implementation of **Pedersen Commitments** for privacy-preserving verifiable transactions.

## Features
- **Perfect Information-Theoretic Hiding**: Commitments reveal nothing about underlying private balances.
- **Computational Binding**: Bound to discrete logarithm hardness over cyclic subgroup generators.
- **Additive Homomorphism**: \(C(v_1, r_1) \cdot C(v_2, r_2) \equiv C(v_1 + v_2, r_1 + r_2) \pmod p\).
- **Zero External Dependencies**: Pure Python standard library.
- **Native MCP Protocol**: JSON-RPC 2.0 stdio server compatible with Claude Desktop, Cursor, and Windsurf.

## Architecture
```mermaid
graph LR
    V1["Value v1, Blinding r1"] --> C1["Commitment C1 = g^v1 * h^r1"]
    V2["Value v2, Blinding r2"] --> C2["Commitment C2 = g^v2 * h^r2"]
    C1 & C2 --> Mult["Multiply mod P"]
    Mult --> CSum["C_sum = C(v1+v2, r1+r2)"]
```
