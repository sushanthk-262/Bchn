import logging
from secret_sharing.blockchain import deploy_contract

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s"
)

if __name__ == '__main__':
    logging.info("Starting contract deployment script...")
    address = deploy_contract()
    logging.info(f"Contract deployed at: {address}")