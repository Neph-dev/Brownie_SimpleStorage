from brownie import SimpleStorage, accounts


def read_contract():
    simple_storage = SimpleStorage[-1]  # Always get the latest transaction.
    print(simple_storage.retrieve())


def main():
    read_contract()
