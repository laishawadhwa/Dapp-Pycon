import json
from web3 import Web3, HTTPProvider
# from web3.contract import ConciseContract
import os
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import EthereumTesterProvider
from web3.middleware import construct_sign_and_send_raw_middleware

# web3.py instance
infura_url = "https://polygon-mumbai.infura.io/v3/<YOUR API KEY>"
w3 = Web3(Web3.HTTPProvider(infura_url))

# w3.middleware_onion.inject(geth_poa_middleware, layer=0)
print(w3.is_connected())

private_key="<Your Private Key>"
acct: LocalAccount = Account.from_key(private_key)

# compile your smart contract with truffle first
truffleFile = json.load(open('./build/contracts/<contract name>.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
contract= w3.eth.contract(bytecode=bytecode, abi=abi)

#building transaction
construct_txn = contract.constructor().build_transaction({
    'from': acct.address,
    'nonce': w3.eth.get_transaction_count(acct.address) + 3,
    'gas': 1728712,
    'gasPrice': w3.to_wei('65', 'gwei')})

signed = acct.sign_transaction(construct_txn)

tx_hash=w3.eth.send_raw_transaction(signed.rawTransaction)
print(tx_hash.hex())
# tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Contract Deployed At:", tx_receipt['status'])

