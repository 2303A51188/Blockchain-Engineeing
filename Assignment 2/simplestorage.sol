// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {

    // State variable to store a number
    uint256 private storedValue;

    // Function to store a value on the blockchain
    function set(uint256 _value) public {
        storedValue = _value;
    }

    // Function to retrieve the stored value
    function get() public view returns (uint256) {
        return storedValue;
    }
}
