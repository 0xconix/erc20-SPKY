from brownie import SpookyToken
from scripts.tools import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, 'ether')

def deploy_spooky_token():
    account = get_account()
    spy = SpookyToken.deploy(initial_supply, {'from': account})
    print(spy.name())

def main():
    deploy_spooky_token()