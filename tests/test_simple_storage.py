# Read the py test documentation for more
from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updated_value():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    new_expected = 77
    simple_storage.store(new_expected, {"from": account})
    # Assert
    assert simple_storage.retrieve() == new_expected
