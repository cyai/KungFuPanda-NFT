from brownie import network, AdvanceCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_character, get_account

character_metadata_dic = {
    "PO":"https://ipfs.io/ipfs/QmdSSaXd2P56s3iRfy3o54XZyHpzAg4GsQ3LrnTYYFnkj3?filename=po.png",
    "CRANE":"https://ipfs.io/ipfs/QmR8y3dxGZChaiqfkRufbdiYqoxYSrYNfgoyxET6sCe9SA?filename=crane.png",
    "MANTIS": "https://ipfs.io/ipfs/QmdZ5vJ3fb5YjWEsxTydbtET2ZhedpJUjUtt1Q3J6Tnnuh?filename=mantis.png",
    "MONKEY": "https://ipfs.io/ipfs/QmSmB2gVvjpChVqaHD7AQPrhF5C42fGg5PuKGJpt7vjgJW?filename=monkey.png",
    "TIGRESS": "https://ipfs.io/ipfs/QmZGSgmGWv2HsMSctZfLeeXQJ2BuFTrXeioy1KtEndKZQo?filename=tigress.png",
    "VIPER": "https://ipfs.io/ipfs/QmQMf24fcHFH276fPWU7Xuf99VczXyB9ncqXyS4HnvDwRX?filename=viper.png",
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