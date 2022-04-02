from brownie import network, AdvanceCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_character, get_account

character_metadata_dic = {
    "PO":"https://ipfs.io/ipfs/QmXSgY6ncZ7dRkoaUcFRHt6nQjfRRWjZqwgaZmco5wVxBV?filename=0-PO.json",
    "CRANE":"https://ipfs.io/ipfs/QmeThTQvZ8uEPU8RmbFXupChGKNhVf87J59qEh3SJGELkL?filename=5-CRANE.json",
    "MANTIS": "https://ipfs.io/ipfs/QmZXPizsSZHJYFCihEFpxQVaVj65Nrp2YhsypxBzMehM6o?filename=2-MANTIS.json",
    "MONKEY": "https://ipfs.io/ipfs/QmUEYp6FFDM1Mv2e1CqNLCAt7xu7f6xGGqtDpZehco674r?filename=4-MONKEY.json",
    "TIGRESS": "https://ipfs.io/ipfs/QmRJbwupW1g5E8N2ep8KQv77k4A1PLAd94qcW6CodNoGCS?filename=2-TIGRESS.json",
    "VIPER": "https://ipfs.io/ipfs/QmS5oP4mYqJGNVHU5edX4Y2SYaN7rhws9C7X7TsktcTUmj?filename=1-VIPER.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvanceCollectible[-1]
    number_of_collectibles = advanced_collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        character = get_character(advanced_collectible.tokenIdtoCharacter(token_id))
        if not advanced_collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, advanced_collectible, character_metadata_dic[character])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 20 minutes, and hit the refresh metadata button")
