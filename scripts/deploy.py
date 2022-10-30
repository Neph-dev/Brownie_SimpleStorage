import os
from brownie import accounts, network, SimpleStorage
from dotenv import load_dotenv

load_dotenv()


def deploy_simple_storage():

    web3_infura_api_key = os.getenv("WEB3_INFURA_API_KEY")

    account = get_account()
    print("Deploying contract ....")
    simple_storage = SimpleStorage.deploy({"from": account})
    print("Deployed!")

    stored_value = simple_storage.retrieve()
    print("The initial value is:", stored_value)

    print("Changing state....")
    trxn = simple_storage.store(15, {"from": account})
    # Wait for trxn to complete.
    trxn.wait(1)
    print("State complete!")

    updated_stored_value = simple_storage.retrieve()
    print("The updated value is:", updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("freecodecamp-account")


def main():
    deploy_simple_storage()
