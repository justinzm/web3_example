# web3py example

### 安装

```python
pip install web3
```

### 使用web3

```python
from web3 import Web3, EthereumTesterProvider
```

#### 测试提供商

```python
w3 = Web3(EthereumTesterProvider())
```

#### 本地提供商

web3.HTTPProvider，用于连接到基于http和https的JSON-RPC服务器。

web3.IPCProvider，用于连接到基于ipc套接字的JSON-RPC服务器。

web3.WebsocketProvider，用于连接基于ws和wss websocket的JSON-RPC服务器。

```python
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))


>>> from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
# Note that you should create only one RPCProvider per
# process, as it recycles underlying TCP/IP network connections between
# your process and Ethereum node
>>> web3 = Web3(HTTPProvider('http://localhost:8545'))

# or for an IPC based connection
>>> web3 = Web3(IPCProvider())

# or for Websocket based connection
>>> web3 = Web3(WebsocketProvider('ws://127.0.0.1:8546'))
```

#### 判断链接状态

```python
w3.isConnected()
```

### 基础接口

#### 类型转换

##### Web3.toHex

采用各种输入并以十六进制表示形式返回。它遵循JSON-RPC规范中转换为十六进制的规则。

**Web3.toHex(primitive=None, hexstr=None, text=None)** 

```
>>> Web3.toHex(0)
'0x0'
>>> Web3.toHex(1)
'0x1'
>>> Web3.toHex(0x0)
'0x0'
>>> Web3.toHex(0x000F)
'0xf'
>>> Web3.toHex(b'')
'0x'
>>> Web3.toHex(b'\x00\x0F')
'0x000f'
>>> Web3.toHex(False)
'0x0'
>>> Web3.toHex(True)
'0x1'
>>> Web3.toHex(hexstr='0x000F')
'0x000f'
>>> Web3.toHex(hexstr='000F')
'0x000f'
>>> Web3.toHex(text='')
'0x'
>>> Web3.toHex(text='cowmö')
'0x636f776dc3b6'
```

##### Web3.toText

接受各种输入并返回其等效字符串。文本被解码为 UTF-8。

**Web3.toText(primitive=None, hexstr=None, text=None)**

```
>>> Web3.toText(0x636f776dc3b6)
'cowmö'
>>> Web3.toText(b'cowm\xc3\xb6')
'cowmö'
>>> Web3.toText(hexstr='0x636f776dc3b6')
'cowmö'
>>> Web3.toText(hexstr='636f776dc3b6')
'cowmö'
>>> Web3.toText(text='cowmö')
'cowmö'
```

##### Web3.toBytes

采用各种输入并返回其等效的字节。文本被编码为UTF-8。

**Web3.toBytes(primitive=None, hexstr=None, text=None)**

```
>>> Web3.toBytes(0)
b'\x00'
>>> Web3.toBytes(0x000F)
b'\x0f'
>>> Web3.toBytes(b'')
b''
>>> Web3.toBytes(b'\x00\x0F')
b'\x00\x0f'
>>> Web3.toBytes(False)
b'\x00'
>>> Web3.toBytes(True)
b'\x01'
>>> Web3.toBytes(hexstr='0x000F')
b'\x00\x0f'
>>> Web3.toBytes(hexstr='000F')
b'\x00\x0f'
>>> Web3.toBytes(text='')
b''
>>> Web3.toBytes(text='cowmö')
b'cowm\xc3\xb6'
```

##### Web3.toInt

采用各种输入并返回其整数等价物。

**Web3.toInt(primitive=None, hexstr=None, text=None)**

```
>>> Web3.toInt(0)
0
>>> Web3.toInt(0x000F)
15
>>> Web3.toInt(b'\x00\x0F')
15
>>> Web3.toInt(False)
0
>>> Web3.toInt(True)
1
>>> Web3.toInt(hexstr='0x000F')
15
>>> Web3.toInt(hexstr='000F')
15
```

#### 货币转换

Web3可以帮助我们在面额之间进行转换

##### Web3.toWei

Web3.toWei(value, currency)   返回转换为wei的 <font color=red>currency</font> 参数指定的面额中的值。

##### Web3.fromWei

Web3.fromWei(value, currency) 返回转换为给定货币的 wei 值。该值以十进制形式返回，以确保精确到 wei。

```
>>> web3.toWei('1', 'ether')
1000000000000000000
>>> web3.fromWei('1000000000000000000', 'ether')
Decimal('1')
>>> from_wei(123456789, 'ether')
Decimal('1.23456789E-10')
```

#### 地址

##### Web3.isAddress(value)

如果值是已识别的地址格式之一，则返回 <font color=red>True</font>。

* 允许 <font color=red>0x</font> 前缀和非 <font color=red>0x</font> 前缀值。

* 如果地址包含混合的大小字符，则此函数还会根据 [EIP55](https://github.com/ethereum/EIPs/issues/55) 检查地址校验和是否有效。

```
>>> web3.isAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
True
```

##### Web3.isChecksumAddress(value)

如果值是有效的 [EIP55](https://github.com/ethereum/EIPs/issues/55) 校验和地址，则返回 <font color=red>True</font>。

```
>>> web3.isChecksumAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
True
>>> web3.isChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
False
```

##### Web3.toChecksumAddress(value)

使用 [EIP55](https://github.com/ethereum/EIPs/issues/55) 校验和返回给定地址。

```
>>> Web3.toChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
'0xd3CdA913deB6f67967B99D67aCDFa1712C293601'
```

#### 加密哈希

##### classmethod Web3.sha3(primitive=None, hexstr=None, text=None)

返回给定值的Keccak SHA256。在计算哈希值之前，文本被编码为UTF-8，就像Solidity一样。以下任何一项都是有效且等效的：

```
>>> Web3.sha3(0x747874)
>>> Web3.sha3(b'\x74\x78\x74')
>>> Web3.sha3(hexstr='0x747874')
>>> Web3.sha3(hexstr='747874')
>>> Web3.sha3(text='txt')
HexBytes('0xd7278090a36507640ea6b7a0034b69b0d240766fa3f98e3722be93c613b29d2e')
```

##### classmethod Web3.soliditySha3(abi_types, value)

返回 sha3，因为它将由提供的 <font color=red>value</font> 和 <font color=red>abi_types</font> 上的solidity <font color=red>sha3</font> 函数计算。 <font color=red>abi_types</font> 值应该是与每个提供的值对应的 solidity 类型字符串的列表。

```ruby
>>> Web3.soliditySha3(['bool'], [True])
HexBytes("0x5fe7f977e71dba2ea1a68e21057beebb9be2ac30c6410aa38d4f3fbe41dcffd2")

>>> Web3.soliditySha3(['uint8', 'uint8', 'uint8'], [97, 98, 99])
HexBytes("0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45")

>>> Web3.soliditySha3(['uint8[]'], [[97, 98, 99]])
HexBytes("0x233002c671295529bcc50b76a2ef2b0de2dac2d93945fca745255de1a9e4017e")

>>> Web3.soliditySha3(['address'], ["0x49eddd3769c0712032808d86597b84ac5c2f5614"])
HexBytes("0x2ff37b5607484cd4eecf6d13292e22bd6e5401eaffcc07e279583bc742c68882")

>>> Web3.soliditySha3(['address'], ["ethereumfoundation.eth"])
HexBytes("0x913c99ea930c78868f1535d34cd705ab85929b2eaaf70fcd09677ecd6e5d75e9")
```

### 查找

#### 查找块
w3.eth.get_block 可以使用API通过它们的编号或哈希来查找块
```python
web3.eth.get_block(1)
web3.eth.get_block('0xf14024701d543b09f4f3047296605373b85347b31a0d6963b6287ba90dc7f324')

# 使用API'latest'中 的字符串检索最新的块
web3.eth.get_block('latest')

# 最新的区块编号
w3.eth.block_number
```

#### 查找交易

web3.eth.getTransaction 函数查找交易

```
>>> web3.eth.getTransaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
{
    'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
    'blockNumber': 46147,
    'condition': None,
    'creates': None,
    'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
    'gas': 21000,
    'gasPrice': 50000000000000,
    'hash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
    'input': '0x',
    'networkId': None,
    'nonce': 0,
    'publicKey': '0x376fc429acc35e610f75b14bc96242b13623833569a5bb3d72c17be7e51da0bb58e48e2462a59897cead8ab88e78709f9d24fd6ec24d1456f43aae407a8970e4',
    'r': '0x88ff6cf0fefd94db46111149ae4bfc179e9b94721fffd821d38d16464b3f71d0',
    'raw': '0xf86780862d79883d2000825208945df9b87991262f6ba471f09758cde1c0fc1de734827a69801ca088ff6cf0fefd94db46111149ae4bfc179e9b94721fffd821d38d16464b3f71d0a045e0aff800961cfce805daef7016b9b675c137a6a41a548f7b60a3484c06a33a',
    's': '0x45e0aff800961cfce805daef7016b9b675c137a6a41a548f7b60a3484c06a33a',
    'standardV': '0x1',
    'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
    'transactionIndex': 0,
    'v': '0x1c',
    'value': 31337,
}
```

#### 查询账户余额

web3.eth.get_balance 查找帐户拥有的以太币数量，请使用该get_balance()方法。
```python
web3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')

# 将该余额转换为以太币
web3.fromWei(99977324660000000000, 'ether')

# 要转换回 wei，您可以使用反函数toWei()
from decimal import Decimal
web3.toWei(Decimal('3841357.360894980500000001'), 'ether')
```

### 合约交互
#### 连接现有合约
```python
address = '0x4598D7e4D91fafbCAdD7D00D381730c2d8569A25'
abi = '[{"inputs":[{"internalType":"string","name":"_name","type":"string"}],"name":"setUser","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getUser","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]'
# 链接合约
contract = web3.eth.contract(address=address, abi=abi)
```

#### 合约交互属性
```python
# 合约地址
Contract.address

# 合约ABI
Contract.abi

# 合约字节码字符串
Contract.bytecode

# 合约字节码字符串的运行时部分
Contract.bytecode_runtime

# 合同的访问功能作为属性
Contract.functions
```

### 案例

#### 在账户之间转移以太币

```
import os
from dotenv import load_dotenv
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/……'))

if w3.isConnected():
    load_dotenv()
    # Account 1
    account1_address = '……'
    account1_private_key = os.getenv('justin01_private_key')
    # Account 2
    account2_address = '……'

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
    # 使用eth.estimate_gas()函数估计此交易需要多少gas，然后将金额插入交易字典
    gas = w3.eth.estimate_gas(tx)
    tx['gas'] = gas
    print(tx)

    # 签署交易
    signed_tx = w3.eth.account.sign_transaction(tx, account1_private_key)

    # 要将交易发送到 Infura，请使用以下eth.send_raw_transaction()函数进行广播交易；返回一个哈希值
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(w3.toHex(tx_hash))

    # 交易需要一些时间来确认。如果要等待事务完成，请使用 eth.wait_for_transaction_receipt()函数
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(receipt)

    print(w3.eth.get_balance(account1_address))
    print(w3.eth.get_balance(account2_address))

else:
    print("未链接区块链")
```

#### 与智能合约交互 01

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8;

contract ProofOfExistence {
    //--- 存储字符串的哈希值 store the hash of the strings---
    mapping (bytes32 => bool) private proofs;
    //--------------------------------------------------
    // 在契约状态下保存存在的证明 Store a proof of existence in the contract state
    //--------------------------------------------------
    function storeProof(bytes32 proof) private {
        // use the hash as the key
        proofs[proof] = true;
    }

    //----------------------------------------------
    // 计算并存储一个文档的证明 Calculate and store the proof for a document
    //----------------------------------------------
    function notarize(string memory document) public {
        // call storeProof() with the hash of the string
        storeProof(proofFor(document));
    }

    //--------------------------------------------
    // 帮助函数获取文档的sha256 Helper function to get a document's sha256
    //--------------------------------------------
    // 接受一个字符串并返回该字符串的散列 Takes in a string and returns the hash of the string
    function proofFor(string memory document) private pure 
    returns (bytes32) {
        // converts the string into bytes array and then hash it
        // 将字符串转换为字节数组，然后对其进行散列
        return sha256(bytes(document));
    }

    //----------------------------------------
    // 检查文件是否经过公证 Check if a document has been notarized
    //----------------------------------------
    function checkDocument(string memory document) public view 
    returns (bool){
        // use the hash of the string and check the proofs mapping
        // object
        return proofs[proofFor(document)];
    }
}
```

```

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
```

#### 与智能合约交互 02

