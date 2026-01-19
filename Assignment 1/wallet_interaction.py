from web3 import Web3


web3 = Web3()

print("Blockchain interface initialized (demo mode)")


PRIVATE_KEY = "0x" + "1" * 64

account = web3.eth.account.from_key(PRIVATE_KEY)


wallet_address = account.address
print("Wallet Address:", wallet_address)


balance_eth = 0
print("Wallet Balance:", balance_eth, "ETH")




transaction = {
    "from": wallet_address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": web3.to_wei(0.01, "ether"),
    "gas": 21000,
    "gasPrice": web3.to_wei(1, "gwei"),
    "nonce": 0
}

print("Transaction prepared successfully (not executed):")
print(transaction)
