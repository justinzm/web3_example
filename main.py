#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2022/6/20 15:19
# @Author : justin.郑 3907721@qq.com
# @File : main.py
# @desc : web3 example


from web3 import Web3, EthereumTesterProvider

# 测试提供商
# w3 = Web3(EthereumTesterProvider())

# 本地提供商
# HTTPProvider:
# w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/6611f2e9846d4bfd97b0104d5d728cbc'))

# 判断链接状态
print(w3.isConnected())

# 查找块
# web3.eth.get_block
# tmp = w3.eth.get_block('0xf14024701d543b09f4f3047296605373b85347b31a0d6963b6287ba90dc7f324')
# 获取最新区块
# tmp = w3.eth.get_block('latest')
# 获取区块数量
# tmp = w3.eth.block_number

# 查询账户余额
# tmp = w3.eth.get_balance("0x7BD8c6F843e4C410Da8a25bf1901Da67715FEbFB")
# 将该余额转换为以太币
# tmp = w3.fromWei(tmp, 'ether')
# print(tmp)

# 查找交易
# tmp = w3.eth.getTransaction('0x21ada7dff3cf4d2daffcecb9bd3d8b589562b19cd678f327f471721642166990')
# print(tmp)

# 与现有合约交互
address = '0x4598D7e4D91fafbCAdD7D00D381730c2d8569A25'
abi = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"}],"name":"setUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getUser","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]'
# 链接合约
# contract = w3.eth.contract(address=address, abi=abi)
# 读取函数
# tmp = contract.functions.getUser().call()
# 写入数据
# tmp = contract.functions.setUser('zm1234').transact({'from':'0x6F976BF89294675D7E3eF755ef2bDEd819F40afD'})
# print(tmp)
# print(contract.all_functions())



# 3 创建账户
# account = w3.eth.account.create()
# print(account.address)

# 获取账户列表
# accounts = w3.eth.accounts
# print(accounts)

# 获取默认账户
# default_account = w3.eth.default_account
# print(default_account)

# 获取余额
# account = '0x50F120861Ca2E647F3CcF7398Fe7759E5BcaF0bd'
# balance = w3.eth.getBalance(account)
# print(balance)

# tmp = w3.isAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
# print(tmp)


# get_transaction_by_block = w3.eth.get_transaction_by_block(2, 0)
# print(get_transaction_by_block)

# tmp = w3.personal.listAccounts
# print(tmp)
