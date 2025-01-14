import nbformat as nbf

# Initialize a new notebook
nb = nbf.v4.new_notebook()

# Define the content for the notebook
content = [
    nbf.v4.new_markdown_cell("# Secret Sharing with Blockchain Integration\n"
                             "This notebook demonstrates how to implement a secret sharing scheme using Python and store/retrieve the shares using a Solidity smart contract on the Ethereum blockchain."),
    
    # Step 1: Secret Sharing Implementation in Python
    nbf.v4.new_code_cell("# Step 1: Secret Sharing Implementation in Python\n"
                         "import random\n"
                         "from sympy import Symbol, interpolate\n\n"
                         "def create_shares(secret, n, t):\n"
                         "    coeffs = [secret] + [random.randint(1, 100) for _ in range(t-1)]\n"
                         "    shares = [(i, sum([coeffs[j] * (i ** j) for j in range(t)])) for i in range(1, n+1)]\n"
                         "    return shares\n\n"
                         "def reconstruct_secret(shares):\n"
                         "    x = Symbol('x')\n"
                         "    points = [(share[0], share[1]) for share in shares]\n"
                         "    polynomial = interpolate(points, x)\n"
                         "    return polynomial.subs(x, 0)\n\n"
                         "# Example usage\n"
                         "secret = 12345\n"
                         "n = 5\n"
                         "t = 3\n\n"
                         "shares = create_shares(secret, n, t)\n"
                         "print('Shares:', shares)\n\n"
                         "# Use first t shares to reconstruct the secret\n"
                         "reconstructed_secret = reconstruct_secret(shares[:t])\n"
                         "print('Reconstructed secret:', reconstructed_secret)"),
    
    # Step 2: Solidity Smart Contract for Storing Shares
    nbf.v4.new_markdown_cell("## Step 2: Solidity Smart Contract for Storing Shares\n"
                             "Below is the Solidity code for storing and retrieving secret shares on the blockchain. You can deploy this contract using Remix IDE or any other Ethereum development environment.\n"
                             "```solidity\n"
                             "// SPDX-License-Identifier: MIT\n"
                             "pragma solidity ^0.8.0;\n\n"
                             "contract SecretSharing {\n"
                             "    struct Share {\n"
                             "        uint256 x;\n"
                             "        uint256 y;\n"
                             "    }\n\n"
                             "    mapping(uint256 => Share) public shares;\n"
                             "    uint256 public sharesCount = 0;\n\n"
                             "    event ShareStored(uint256 indexed shareId, uint256 x, uint256 y);\n\n"
                             "    function storeShare(uint256 x, uint256 y) public {\n"
                             "        sharesCount++;\n"
                             "        shares[sharesCount] = Share(x, y);\n"
                             "        emit ShareStored(sharesCount, x, y);\n"
                             "    }\n\n"
                             "    function getShare(uint256 shareId) public view returns (uint256, uint256) {\n"
                             "        require(shareId > 0 && shareId <= sharesCount, 'Share does not exist.');\n"
                             "        Share memory share = shares[shareId];\n"
                             "        return (share.x, share.y);\n"
                             "    }\n"
                             "}\n"
                             "```"),
    
    # Step 3: Interact with the Smart Contract Using Python and web3.py
    nbf.v4.new_markdown_cell("## Step 3: Interact with the Smart Contract Using Python and web3.py\n"
                             "The following Python code demonstrates how to interact with the deployed smart contract to store and retrieve shares."),
    nbf.v4.new_code_cell("from web3 import Web3\n"
                         "import json\n\n"
                         "# Connect to local Ethereum node\n"
                         "web3 = Web3(Web3.HTTPProvider('http://localhost:8545'))\n\n"
                         "# Replace with your deployed contract address\n"
                         "contract_address = '0xYourContractAddress'\n\n"
                         "# Replace with your contract's ABI\n"
                         "contract_abi = json.loads('[{\"inputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"constructor\"},"
                         "{\"anonymous\":false,\"inputs\":[{\"indexed\":true,\"internalType\":\"uint256\",\"name\":\"shareId\",\"type\":\"uint256\"},"
                         "{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"x\",\"type\":\"uint256\"},"
                         "{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"y\",\"type\":\"uint256\"}],\"name\":\"ShareStored\",\"type\":\"event\"},"
                         "{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"shareId\",\"type\":\"uint256\"}],\"name\":\"getShare\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"},"
                         "{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},"
                         "{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"x\",\"type\":\"uint256\"},"
                         "{\"internalType\":\"uint256\",\"name\":\"y\",\"type\":\"uint256\"}],\"name\":\"storeShare\",\"outputs\":[],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},"
                         "{\"inputs\":[],\"name\":\"sharesCount\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},"
                         "{\"inputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"name\":\"shares\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"x\",\"type\":\"uint256\"},"
                         "{\"internalType\":\"uint256\",\"name\":\"y\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"}]')\n\n"
                         "# Create contract instance\n"
                         "contract = web3.eth.contract(address=contract_address, abi=contract_abi)\n\n"
                         "# Function to store a share\n"
                         "def store_share(x, y):\n"
                         "    tx_hash = contract.functions.storeShare(x, y).transact({'from': web3.eth.accounts[0]})\n"
                         "    receipt = web3.eth.waitForTransactionReceipt(tx_hash)\n"
                         "    return receipt\n\n"
                         "# Function to get a share by ID\n"
                         "def get_share(share_id):\n"
                         "    share = contract.functions.getShare(share_id).call()\n"
                         "    return share\n\n"
                         "# Example usage\n"
                         "if __name__ == '__main__':\n"
                         "    secret = 12345\n"
                         "    n = 5\n"
                         "    t = 3\n\n"
                         "    # Create shares\n"
                         "    shares = create_shares(secret, n, t)\n"
                         "    print('Shares:', shares)\n\n"
                         "    # Store shares on blockchain\n"
                         "    for share in shares:\n"
                         "        store_share(share[0], share[1])\n\n"
                         "    # Retrieve shares from blockchain and reconstruct secret\n"
                         "    retrieved_shares = [get_share(i) for i in range(1, t+1)]\n"
                         "    print('Retrieved shares:', retrieved_shares)\n\n"
                         "    reconstructed_secret = reconstruct_secret(retrieved_shares)\n"
                         "    print('Reconstructed secret:', reconstructed_secret)")
]

# Add cells to the notebook
nb.cells.extend(content)

# Write the notebook to a file
notebook_path = 'Secret_Sharing_with_Blockchain.ipynb'
with open(notebook_path, 'w') as f:
    nbf.write(nb, f)

# # Verify if the file exists
# os.path.exists(notebook_path), notebook_path
