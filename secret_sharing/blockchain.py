import logging
from web3 import Web3
from .config import INFURA_URL, WALLET_ADDRESS, PRIVATE_KEY, CONTRACT_ABI, CONTRACT_BYTECODE, SEPOLIA_CHAIN_ID

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def deploy_contract():
    logging.info("Preparing to deploy contract...")
    contract = web3.eth.contract(abi=CONTRACT_ABI, bytecode=CONTRACT_BYTECODE)
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
    tx = contract.constructor().build_transaction({
        'gas': 3000000,
        'gasPrice': web3.eth.gas_price,
        'chainId': SEPOLIA_CHAIN_ID,
        'from': WALLET_ADDRESS,
        'nonce': nonce
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    logging.info(f"Contract deployment transaction sent: {tx_hash.hex()}")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    logging.info(f"Contract deployed at address: {receipt.contractAddress}")
    return receipt.contractAddress

def store_share(x, y, contract_address):
    logging.info(f"Storing share (x={x}, y={y}) to contract {contract_address}...")
    contract = web3.eth.contract(address=contract_address, abi=CONTRACT_ABI)
    nonce = web3.eth.get_transaction_count(WALLET_ADDRESS)
    tx = contract.functions.storeShare(x, y).build_transaction({
        'gas': 300000,
        'gasPrice': web3.eth.gas_price,
        'chainId': SEPOLIA_CHAIN_ID,
        'from': WALLET_ADDRESS,
        'nonce': nonce
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)
    logging.info(f"Share storage transaction sent: {tx_hash.hex()}")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    logging.info(f"Share stored. Transaction receipt: {receipt.transactionHash.hex()}")
    return receipt

def get_share(share_id, contract_address):
    logging.info(f"Retrieving share with ID {share_id} from contract {contract_address}...")
    contract = web3.eth.contract(address=contract_address, abi=CONTRACT_ABI)
    share = contract.functions.getShare(share_id).call()
    logging.info(f"Retrieved share: {share}")
    return share