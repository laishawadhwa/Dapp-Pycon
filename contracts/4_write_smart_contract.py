import json
from web3 import Web3


# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))



# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[0]
# Greeter contract ABI
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# Greeter contract address - convert to checksum address
address = web3.to_checksum_address('0xdBf27379664e533c472D50c16772cd83751a06ca') # FILL ME IN with the deployed address of your contract
# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)
# Read the default greeting
print(contract.functions.getGreeting().call())
# Set a new greeting
tx_hash = contract.functions.setGreeting('HEELLLLOOOOOO Updated!!!').transact()
# Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)
# Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.getGreeting().call()
))
