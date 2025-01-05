from web3 import Web3

# Connect to the local Ganache blockchain
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Check connection
if w3.is_connected():
    print("Connected to Ganache")
else:
    raise ConnectionError("Failed to connect to Ganache")

# Load the compiled contract ABI
with open(r'C:\Users\GVH VARDHAN\Desktop\Random_shit\Block Chain\build\SimpleContract_sol_SimpleContract.abi', 'r') as file:
    contract_abi = file.read()

# Load the contract bytecode
with open(r'C:\Users\GVH VARDHAN\Desktop\Random_shit\Block Chain\build\SimpleContract_sol_SimpleContract.bin', 'r') as file:
    contract_bytecode = file.read()

# Get the first Ganache account for deployment
accounts = w3.eth.accounts
print(f"Available accounts: {accounts}")
deployer_account = accounts[0]

# Create a contract instance
SimpleContract = w3.eth.contract(abi=contract_abi, bytecode=contract_bytecode)

# Deploy the contract with a gas limit
try:
    transaction_hash = SimpleContract.constructor().transact({
        'from': deployer_account,
        'gas': 3000000  # Adjust gas limit if needed
    })
    print(f"Transaction hash: {transaction_hash.hex()}")

    # Wait for transaction receipt
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    contract_address = transaction_receipt['contractAddress']
    print(f"Contract deployed at address: {contract_address}")

except Exception as e:
    print(f"Deployment failed: {e}")
