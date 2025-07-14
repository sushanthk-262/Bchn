# Secret Sharing with Blockchain

This project demonstrates Shamir's Secret Sharing integrated with an Ethereum smart contract using Python and Solidity.

## Structure

- `contracts/`: Solidity smart contract
- `secret_sharing/`: Python package for secret sharing and blockchain interaction
- `scripts/`: Example scripts for deploying and using the contract
- `tests/`: Unit tests

## Usage

1. Deploy the contract:  
   `python scripts/deploy_contract.py`

2. Store shares:  
   Edit `CONTRACT_ADDRESS` in `store_shares.py`, then  
   `python scripts/store_shares.py`

3. Retrieve and reconstruct:  
   Edit `CONTRACT_ADDRESS` in `retrieve_and_reconstruct.py`, then  
   `python scripts/retrieve_and_reconstruct.py`