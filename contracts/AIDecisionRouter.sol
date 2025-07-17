// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/// @title AI Decision Router - Stores and manages AI-based decision outcomes on-chain
/// @notice This contract acts as a simple router for AI decisions, enabling other contracts or users to query and verify AI outputs.
/// @dev Assumes AI computation is off-chain. Only decisions are stored on-chain.

contract AIDecisionRouter {
    address public owner;

    // Decision structure: id, outcome (bool, uint, etc), timestamp
    struct Decision {
        uint256 id;
        bool approved; // example: AI approved transaction or flagged it
        uint256 timestamp;
        string metadata; // optional JSON or description
    }

    // Mapping of decision ID to Decision
    mapping(uint256 => Decision) public decisions;

    // Latest decision ID tracker
    uint256 public latestDecisionId;

    // Events
    event DecisionCreated(uint256 indexed id, bool approved, string metadata, uint256 timestamp);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /// @notice Register a new AI decision
    /// @param _approved The boolean decision from AI (approved/rejected)
    /// @param _metadata Optional metadata about decision (e.g. AI model version, notes)
    function registerDecision(bool _approved, string calldata _metadata) external onlyOwner returns (uint256) {
        latestDecisionId++;
        decisions[latestDecisionId] = Decision({
            id: latestDecisionId,
            approved: _approved,
            timestamp: block.timestamp,
            metadata: _metadata
        });

        emit DecisionCreated(latestDecisionId, _approved, _metadata, block.timestamp);
        return latestDecisionId;
    }

    /// @notice Change contract owner
    /// @param _newOwner Address of new owner
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Zero address not allowed");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /// @notice Fetch a decision by ID
    /// @param _id Decision ID
    /// @return Decision struct
    function getDecision(uint256 _id) external view returns (Decision memory) {
        return decisions[_id];
    }
}
