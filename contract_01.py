#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/9/6 14:34
# @Author : justin.郑 3907721@qq.com
# @File : contract_01.py
# @desc : 与智能合约交互 01 ; contract_01.py

import os
from web3 import Web3
from dotenv import load_dotenv

w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

if w3.isConnected():
    load_dotenv()
    # 获取账户列表
    accounts = w3.eth.accounts
    account4_address = accounts[4]
    account4_private_key = os.environ.get('ganache_account_key_04')

    # 与现有合约交互
    address = '0xF8A1778c005020FE524B98EA0052eBd0C0055AaA'
    abi = '[{"inputs":[{"internalType":"string","name":"document","type":"string"}],"name":"notarize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"document","type":"string"}],"name":"checkDocument","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"}]'

    # 链接合约 通过将合约的地址和 ABI 传递给eth.contract()函数来创建对它的引用
    contract = w3.eth.contract(address=address, abi=abi)

    string_to_notarise = "Ofenbach — You Don't Know Me"

    # 获取从指定账户发送的交易数量。这将用作交易的随机数。
    nonce = w3.eth.get_transaction_count(account4_address)

    # 估计调用notarize()合约函数所需的gas
    estimated_gas = contract.functions.notarize(string_to_notarise).estimate_gas()

    # 构建交易以对字符串进行公证 build the transaction
    transaction = contract.functions.notarize(string_to_notarise).build_transaction(
        {
            'gas': estimated_gas,
            'gasPrice': w3.eth.gas_price,
            'from': account4_address,
            'nonce': nonce
        })

    # 签署交易 sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key=account4_private_key)
    # 发送交易 send the transaction
    tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print(w3.toHex(tx_hash))
    # 等待交易确认 wait for the transaction to confirm
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)

    # check if string is notarized correctly
    # tmp = contract.functions.checkDocument(string_to_notarise).call()
    # print(tmp)

else:
    print("未链接区块链")