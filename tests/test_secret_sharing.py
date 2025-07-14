from secret_sharing.core import create_shares, reconstruct_secret

def test_secret_sharing():
    secret = 12345
    n = 5
    t = 3
    shares = create_shares(secret, n, t)
    reconstructed = reconstruct_secret(shares[:t])
    assert reconstructed == secret