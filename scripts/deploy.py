from brownie import accounts, config, SimpleStorage

def deploy_simple_storage():
     # account = accounts.add(config["wallets"]["from_key"])
     account = accounts[0]
     simple_storage = SimpleStorage.deploy({"from": account})
     print(simple_storage)

     # a simple retrieve from the contract, calling the retrieve function on contract
     stored_value = simple_storage.retrieve()
     print(stored_value)

     # calling a transaction function
     # note: In browniew, we need to pass the from account with the call
     transaction = simple_storage.store(15, {"from": account})
     transaction.wait(1)

     # retrieve the latest state from the chain
     updated_stored_value = simple_storage.retrieve()
     print(updated_stored_value)



def main():
     deploy_simple_storage()
     print("Hello")