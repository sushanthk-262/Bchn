// SPDX-License-Identifier: MIT
pragma solidity 0.8.26;

contract SecretSharing {
    struct Share {
        uint256 x;
        uint256 y;
    }

    Share[] public shares;

    event ShareStored(uint256 indexed shareId, uint256 x, uint256 y);

    function storeShare(uint256 x, uint256 y) public {
        shares.push(Share(x, y));
        emit ShareStored(shares.length - 1, x, y);
    }

    function getShare(uint256 shareId) public view returns (uint256, uint256) {
        Share memory share = shares[shareId];
        return (share.x, share.y);
    }
}