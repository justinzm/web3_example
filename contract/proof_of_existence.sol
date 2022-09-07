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