# KungFuPanda-NFT

![Kung Fu Panda NFT](img/1607060108536.png)

Welcome to the Kung Fu Panda Movie Series Character NFT project! This repository contains the smart contracts, metadata, and scripts required to create unique NFTs for characters from the beloved Kung Fu Panda movie series.

## Table of Contents
- [Introduction](#introduction)
- [Contracts](#contracts)
- [Metadata](#metadata)
- [Scripts](#scripts)
- [Getting Started](#getting-started)
- [License](#license)

## Introduction

In this project, we aim to tokenize characters from the Kung Fu Panda movie series as Non-Fungible Tokens (NFTs). Each NFT will represent a unique character, allowing fans and collectors to own and trade their favorite characters from the movie.

## Contracts

The `contracts` directory contains the smart contract source code used to create the Kung Fu Panda NFTs. The main contract responsible for the NFT functionality is `AdvanceCollectible.sol`.

- [AdvanceCollectible.sol](contracts/AdvanceCollectible.sol) - Smart contract to create and manage the Kung Fu Panda NFTs.

## Metadata

The `metadata` directory houses the metadata files associated with each Kung Fu Panda NFT. Metadata includes information about the character, such as name, image, description, and other relevant attributes.

## Scripts

The `scripts` directory contains various scripts used for managing and deploying the smart contracts and metadata. One notable script is `set_tokenuri.py`, responsible for setting the metadata URI for each NFT.

- [set_tokenuri.py](scripts/set_tokenuri.py) - Script to set the metadata URI for Kung Fu Panda NFTs.

## Getting Started

To get started with the Kung Fu Panda NFT project, follow these steps:

1. Clone the repository locally using `git clone https://github.com/cyai/KungFuPanda-NFT.git`.
2. Install the required dependencies using [Brownie](https://github.com/eth-brownie/brownie) by running `pip install eth-brownie`.
3. Deploy the smart contract using [Brownie](https://github.com/eth-brownie/brownie) by executing `brownie run deploy`.
4. Customize and set metadata for each NFT using `set_tokenuri.py` script.
5. Interact with the deployed smart contract to mint and trade Kung Fu Panda NFTs.

Feel free to explore the repository and its various components to understand how the NFTs are created and managed.

## License

This project is licensed under the [MIT License](LICENSE), allowing you to modify and distribute the codebase as you see fit.

Happy NFT creating!
