from brownie import network, config, accounts, MockV3Aggregator

FORKED_BLOCKCHAINS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_DEVELOPMENT_CHAIN = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_DEVELOPMENT_CHAIN
        or network.show_active() in FORKED_BLOCKCHAINS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed..!")
