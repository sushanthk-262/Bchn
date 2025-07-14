import logging
from secret_sharing.core import create_shares, reconstruct_secret
from secret_sharing.blockchain import deploy_contract, store_share, get_share

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s"
)

def main():
    # Step 1: Deploy contract
    logging.info("Deploying contract...")
    contract_address = deploy_contract()
    logging.info(f"Contract deployed at: {contract_address}")

    # Step 2: Create shares
    secret = 12345
    n = 5
    t = 3
    shares = create_shares(secret, n, t)
    logging.info(f"Created shares: {shares}")

    # Step 3: Store shares on blockchain
    logging.info("Storing shares on blockchain...")
    for x, y in shares:
        store_share(x, y, contract_address)
    logging.info("All shares stored.")

    # Step 4: Retrieve shares from blockchain
    logging.info(f"Retrieving {t} shares from blockchain...")
    retrieved_shares = [get_share(i, contract_address) for i in range(t)]
    logging.info(f"Retrieved shares: {retrieved_shares}")

    # Step 5: Reconstruct secret
    reconstructed = reconstruct_secret(retrieved_shares)
    logging.info(f"Reconstructed secret: {reconstructed}")

if __name__ == "__main__":
    main()