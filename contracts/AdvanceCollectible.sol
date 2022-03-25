// SPDX-Licence-Identifier: MIT

pragma solidity ^0.6.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvanceCollectible is ERC721, VRFConsumerBase {
    bytes32 public keyhash;
    uint256 public fee;
    uint256 public tokenCounter;

    enum Characters{PO,TIGRESS,MOKEY,CRANE,MANTIS,VIPER}

    mapping(bytes32 => address) public requestIdtoSender;
    mapping(uint256 => Characters) public tokenIdtoBreed;

    event requestedCollectible(bytes32 indexed requestId, address requestor);
    event breedAssigned(uint256 indexed tokenId, Characters character);

    constructor(address _vrfCoordinator, address _link, bytes32 _keyhash, uint256 _fee) public
    VRFConsumerBase(_vrfCoordinator, _link)
    ERC721("KungFu","KUNGFU"){
        keyhash = _keyhash;
        fee = _fee;
        tokenCounter = 0;
    }

    function createCollectible() public returns(bytes32){
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdtoSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);

    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override{
        Characters character = Characters(randomNumber % 6);
        uint256 newTokenId = tokenCounter;
        tokenIdtoBreed[newTokenId] = character;
        emit breedAssigned(newTokenId, character);
        address owner = requestIdtoSender[requestId];
        _safeMint(owner, newTokenId);
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public{
        require(_isApprovedOrOwner(msg.sender, tokenId), "ERC721: caller is not owner no approved");
        _setTokenURI(tokenId, _tokenURI);
    }
}

