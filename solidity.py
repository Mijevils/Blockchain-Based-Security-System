from web3 import Web3
import json


class Connect():
    def __init__(self):
        self.w3 = self.connect()
        self.lastContract = None
        self.currentContract = None

    def connect(self):
        """
        Description: Establishes a connection to an ETH node
        Input: None, just self
        Output: Returns the connection value w3
        """
        w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        # Check if the connection is successful
        if w3.is_connected():
            print("Connected to Ethereum node")
            return w3
        else:
            print("Failed to connect to Ethereum node")

    def deployContract(self, superhash):
        """
        Description: Deploys contract with superhash
        Input: Superhash string
        Output: None, but uploads contract to the blockchain
        """
        self.lastContract = self.currentContract
        with open('artifacts\\contracts\\hash.sol\\StringStorage.json') as f:
            self.currentContract = json.load(f)

        abi = self.currentContract['abi']
        bytecode = self.currentContract['bytecode']

        # Set your wallet private key (for local testing purposes)
        private_key = '0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80'  # account #0

        # Deploy the contract
        contract = self.w3.eth.contract(abi=abi, bytecode=bytecode)
        deploy_transaction = contract.constructor(superhash).build_transaction({
            'from': self.w3.eth.accounts[0],  # Use the first account for deployment
            'gas': 2000000,  # Adjust gas limit as needed
            'gasPrice': self.w3.to_wei('20', 'gwei'),  # Adjust gas price as needed
            'nonce': self.w3.eth.get_transaction_count(self.w3.eth.accounts[0]),
        })

        print("Contract deployed")
        signed_transaction = self.w3.eth.account.sign_transaction(deploy_transaction, private_key)
        transaction_hash = self.w3.eth.send_raw_transaction(signed_transaction.rawTransaction)

        # Wait for the deployment transaction to be mined
        transaction_receipt = self.w3.eth.wait_for_transaction_receipt(transaction_hash)

        # Contract address
        self.currentContract['address'] = transaction_receipt['contractAddress']


    def getHash(self):
        address = self.lastContract['address']
        abi = self.lastContract['abi']
        contract = self.w3.eth.contract(abi=abi, address=address)
        hash = contract.functions.getString().call()
        print('Hash:', hash)

        return hash

