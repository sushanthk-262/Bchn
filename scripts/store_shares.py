import logging
from secret_sharing.core import create_shares
from secret_sharing.blockchain import store_share

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s"
)

CONTRACT_ADDRESS = '...'  # Fill in after deployment

secret = 12345
n = 5
t = 3
logging.info(f"Creating {n} shares with threshold {t} for secret {secret}...")
shares = create_shares(secret, n, t)
logging.info(f"Created shares: {shares}")
for x, y in shares:
    logging.info(f"Storing share (x={x}, y={y})...")
    store_share(x, y, CONTRACT_ADDRESS)
logging.info("All shares stored on blockchain.")