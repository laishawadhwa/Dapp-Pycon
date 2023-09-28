from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/<YOUR API KEY>"
web3 = Web3(Web3.HTTPProvider(infura_url))

print("Coneection status: ", web3.is_connected())

block = web3.eth.get_block('latest')
print("Latest Block number: ", block['number'])

# Fill in your account here
balance = web3.eth.get_balance("abc.eth") # or your ENS example abc.eth
print("balance for account: ", web3.from_wei(balance, "ether"), "ETH")
