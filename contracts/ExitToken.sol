// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ExitToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("Exit Token", "EXIT") {
        _mint(msg.sender, initialSupply);
    }
}
