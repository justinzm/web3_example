#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/9/29 11:31
# @Author : justin.郑 3907721@qq.com
# @File : zombies.py
# @desc : 僵尸工厂 案例

import os
from dotenv import load_dotenv
from web3 import Web3


w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

if w3.isConnected():
    load_dotenv()
    print("ok")
    address = '0x42643cF3315923F2984057912199717E50aa4889'
    abi = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"}],"name":"createRandomZombie","outputs":[],"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"zombieId","type":"uint256"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint256","name":"dna","type":"uint256"}],"name":"NewZombie","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"zombies","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"dna","type":"uint256"}],"stateMutability":"view","type":"function"}]'

    # 链接合约 通过将合约的地址和 ABI 传递给eth.contract()函数来创建对它的引用
    contract = w3.eth.contract(address=address, abi=abi)

    # Account 1
    account1_address = '0x0E1436B9e4e0f2386Ecd8A20fD030D5C4AC9702D'
    account1_private_key = os.getenv('account_05')

    option = {
        'from': account1_address,
        'gas': 1000000
    }

    tmp = contract.functions.createRandomZombie("justin").transact(option)

    print(tmp)