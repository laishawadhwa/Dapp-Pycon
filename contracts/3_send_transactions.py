from web3 import Web3

ganache_url = "http://127.0.0.1:7545"  # ganache URL can be polygon testnet or sepolia test net as well
web3 = Web3(Web3.HTTPProvider(ganache_url))


account_1 = '' # Fill me in
account_2 = '' # Fill me in
private_key = '' # Fill me in

nonce = web3.eth.get_transaction_count(account_1)

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
# print(signed_tx)

print("balances before txn")
print("Balance of Sender Account:", web3.from_wei(web3.eth.get_balance(account_1), 'ether'), "Balance of receiver account: ", web3.from_wei(web3.eth.get_balance(account_2), 'ether'))

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("Txn Hash:", web3.to_hex(tx_hash))
print("Balance of Sender Account:", web3.from_wei(web3.eth.get_balance(account_1), 'ether'), "Balance of receiver account: ", web3.from_wei(web3.eth.get_balance(account_2), 'ether'))
