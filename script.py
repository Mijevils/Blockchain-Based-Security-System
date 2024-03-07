from web3 import Web3

# Connect to the local Hardhat Network
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Load compiled contract
with open('hardhat\artifacts\contracts\hash.sol\StringStorage.json') as f:
    contract_data = json.load(f)

abi = contract_data['abi']
bytecode = contract_data['bytecode']

# Set your wallet private key (for local testing purposes)
private_key = 'your_private_key'

print("We good till here")
# Deploy the contract
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
deploy_transaction = contract.constructor().buildTransaction({
    'from': w3.eth.accounts[0],  # Use the first account for deployment
    'gas': 2000000,  # Adjust gas limit as needed
    'gasPrice': w3.toWei('20', 'gwei'),  # Adjust gas price as needed
    'nonce': w3.eth.getTransactionCount(w3.eth.accounts[0]),
})

print("I think deployed")
signed_transaction = w3.eth.account.sign_transaction(deploy_transaction, private_key)
transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

# Wait for the deployment transaction to be mined
transaction_receipt = w3.eth.waitForTransactionReceipt(transaction_hash)

# Contract address
contract_address = transaction_receipt['contractAddress']
