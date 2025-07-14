from secret_sharing.core import reconstruct_secret
from secret_sharing.blockchain import get_share

CONTRACT_ADDRESS = '...'  # Fill in after deployment
t = 3

retrieved_shares = [get_share(i, CONTRACT_ADDRESS) for i in range(t)]
secret = reconstruct_secret(retrieved_shares)
print("Reconstructed secret:", secret)