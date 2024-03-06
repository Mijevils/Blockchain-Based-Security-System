// SPDX-License-Identifier: MIT
pragma solidity >=0.6.12 <0.9.0;

contract StringStorage {
    // Declare a state variable to store the string
    string private superHash;

    // Event to log when the string is updated
    event StringUpdated(string newString);

    // Function to set the string
    function setString(string memory newString) public {
        superHash = newString;
        emit StringUpdated(newString);
    }

    // Function to get the stored string
    function getString() public view returns (string memory) {
        return superHash;
    }
}

      