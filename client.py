"""Pedersen Commitment Scheme.
100% Python Standard Library.
"""

class PedersenCommitment:
    """Additively homomorphic Pedersen commitment over prime order group."""
    P = 2147483647
    G = 7
    H = 11

    @classmethod
    def commit(cls, value, blinding_factor):
        c = (pow(cls.G, value, cls.P) * pow(cls.H, blinding_factor, cls.P)) % cls.P
        return c

    @classmethod
    def verify(cls, commitment, value, blinding_factor):
        expected = cls.commit(value, blinding_factor)
        return commitment == expected

    @classmethod
    def add_commitments(cls, c1, c2):
        return (c1 * c2) % cls.P
