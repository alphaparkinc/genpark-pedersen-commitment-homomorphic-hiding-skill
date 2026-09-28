from client import PedersenCommitment

c1 = PedersenCommitment.commit(100, 42)
c2 = PedersenCommitment.commit(250, 77)

c_sum = PedersenCommitment.add_commitments(c1, c2)
print("Homomorphic verification of sum (100 + 250 = 350):")
print(PedersenCommitment.verify(c_sum, 350, 42 + 77))
