from web3 import Web3

class Connect():
    def __init__(self):
        self.w3 = self.connect()
        self.contract = self.loadContract()

    def connect(self):
        w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
        # Check if the connection is successful
        if w3.isConnected():
            print("Connected to Ethereum node")
            return w3
        else:
            print("Failed to connect to Ethereum node")

    def loadContract(self):
        # Replace with your contract ABI and address
        contract_abi = [
            {
                "anonymous": false,
                "inputs": [
                    {
                        "indexed": false,
                        "internalType": "string",
                        "name": "newString",
                        "type": "string"
                    }
                ],
                "name": "StringUpdated",
                "type": "event"
            },
            {
                "inputs": [],
                "name": "getString",
                "outputs": [
                    {
                        "internalType": "string",
                        "name": "",
                        "type": "string"
                    }
                ],
                "stateMutability": "view",
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "internalType": "string",
                        "name": "newString",
                        "type": "string"
                    }
                ],
                "name": "setString",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
            }
        ]
        contract_address = '0xd9145CCE52D386f254917e481eB44e9943F39138'  # Ethereum address of the deployed contract

        # Create a contract instance
        contract = self.w3.eth.contract(address=contract_address, abi=contract_abi)

        return contract

    def uploadString(self, superhash):
        # Call a function that requires a transaction
        account = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"  # Replace with your Ethereum account address
        private_key = '0xabcdef...'  # Replace with your private key
        gas_limit = 100000  # Replace with an appropriate gas limit

        transaction = self.contract.functions.setString(newString).buildTransaction({
            'from': account,
            'gas': gas_limit,
            'gasPrice': self.w3.toWei('20', 'gwei'),
            'nonce': self.w3.eth.getTransactionCount(account),
        })

        signed_transaction = self.w3.eth.account.signTransaction(transaction, private_key)
        tx_hash = self.w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

        print("Transaction Hash:", tx_hash)

    def retrieveString(self):
        # Call the getString function that doesn't require a transaction (view function)
        result = self.contract.functions.getString().call()
        print("Retrieved String:", result)


connector = Connect()
connector.uploadString("NewString123")
connector.retrieveString()