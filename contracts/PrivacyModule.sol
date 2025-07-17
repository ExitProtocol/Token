// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PrivacyModule {
    mapping(address => bytes32) private commitments;

    event CommitmentAdded(address indexed user, bytes32 commitment);

    function addCommitment(bytes32 commitment) public {
        commitments[msg.sender] = commitment;
        emit CommitmentAdded(msg.sender, commitment);
    }

    function verifyCommitment(address user, bytes32 commitment) public view returns (bool) {
        return commitments[user] == commitment;
    }
}
