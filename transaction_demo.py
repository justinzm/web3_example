#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/9/5 10:56
# @Author : justin.郑 3907721@qq.com
# @File : transaction_demo.py
# @desc : 账户之间转移以太币 交易Demo

import os
from dotenv import load_dotenv
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/6611f2e9846d4bfd97b0104d5d728cbc'))

if w3.isConnected():
    load_dotenv()
    # Account 1
    account1_address = '0xeC1E733c8AF68160931A8Cd1A316F347cEDEc1c1'
    account1_private_key = os.getenv('justin01_private_key')
    # Account 2
    account2_address = '0x9A5E140d5a4538afE752b266765D724557Dedb91'

    # 获取账户余额
    print(w3.eth.get_balance(account1_address))

    # 在账户之间转移以太币
    # 首先使用eth.get_transaction_count()函数获取从指定账户发送的交易数量。这将用作交易的随机数。
    # 然后，创建一个包含交易详情的字典：
    nonce = w3.eth.get_transaction_count(account1_address)
    tx = {
        'nonce': nonce,                      # transaction count
        'to': account2_address,              # who to send the ETH to
        'value': w3.toWei(1, 'ether'),       # the amount to transfer
        'gasPrice': w3.eth.gas_price,        # get the price of gas
    }
    gas = w3.eth.estimate_gas(tx)
    tx['gas'] = gas
    print(tx)

    # 签署交易
    signed_tx = w3.eth.account.sign_transaction(tx, account1_private_key)

    # 要将交易发送到 Infura，请使用以下eth.send_raw_transaction()函数
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(w3.toHex(tx_hash))

    # 交易需要一些时间来确认。如果要等待事务完成，请使用 eth.wait_for_transaction_receipt()函数
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)

    print(w3.eth.get_balance(account1_address))
    print(w3.eth.get_balance(account2_address))

else:
    print("未链接区块链")

