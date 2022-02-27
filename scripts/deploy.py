from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helping_scripts import LOCAL_DEVELOPMENT_CHAIN, get_account, deploy_mocks


def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_DEVELOPMENT_CHAIN:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()