import pytest
from scripts.helping_scripts import LOCAL_DEVELOPMENT_CHAIN, get_account
from scripts.deploy import deploy_fund_me
from brownie import accounts, network, exceptions


def test_fund_withdraw():
    account = get_account()
    fundMe = deploy_fund_me()
    enterance_fee = fundMe.getEntranceFee()
    txn = fundMe.fund({"from": account, "value": enterance_fee})
    txn.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == enterance_fee
    txn2 = fundMe.withdraw({"from": account})
    txn2.wait(1)
    assert fundMe.addressToAmountFunded(account.address) == 0


def test_ifOwner_can_only_withdraw():
    if network.show_active() not in LOCAL_DEVELOPMENT_CHAIN:
        pytest.skip("ONLY FOR LOCAL TESTING!")
    fundMe = deploy_fund_me()
    Bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({"from": Bad_actor})
