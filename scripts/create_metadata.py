from brownie import AdvanceCollectible, network
from scripts.helpful_scripts import get_character
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

character_to_image_uri = {
    "PO":"https://ipfs.io/ipfs/QmdSSaXd2P56s3iRfy3o54XZyHpzAg4GsQ3LrnTYYFnkj3?filename=po.png",
    "CRANE":"https://ipfs.io/ipfs/QmR8y3dxGZChaiqfkRufbdiYqoxYSrYNfgoyxET6sCe9SA?filename=crane.png",
    "MANTIS": "https://ipfs.io/ipfs/QmdZ5vJ3fb5YjWEsxTydbtET2ZhedpJUjUtt1Q3J6Tnnuh?filename=mantis.png",
    "MONKEY": "https://ipfs.io/ipfs/QmSmB2gVvjpChVqaHD7AQPrhF5C42fGg5PuKGJpt7vjgJW?filename=monkey.png",
    "TIGRESS": "https://ipfs.io/ipfs/QmZGSgmGWv2HsMSctZfLeeXQJ2BuFTrXeioy1KtEndKZQo?filename=tigress.png",
    "VIPER": "https://ipfs.io/ipfs/QmQMf24fcHFH276fPWU7Xuf99VczXyB9ncqXyS4HnvDwRX?filename=viper.png",
}


def main():
    advanced_collectible = AdvanceCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_advanced_collectibles} collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        character = get_character(advanced_collectible.tokenIdtoCharacter(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{character}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating Metadata file: {metadata_file_name}")
            collectible_metadata["name"] = character
            match character.upper():
                case "PO":
                    collectible_metadata["description"] = "Master Po Ping (known simply as Po, and originally named Lotus[1]) is the main protagonist of the Kung Fu Panda franchise. He is the adopted son of Mr. Ping and the biological son of Li Shan and Li's wife, as well as one of Master Shifu's students at the Jade Palace. He is also the foretold Dragon Warrior of legend, and a master of the Panda Style of kung fu. "
                case "TIGRESS":
                    collectible_metadata["description"] = "Master Tigress is one of the main supporting characters of the Kung Fu Panda franchise. She is a member of the Furious Five as well as one of Master Shifu's students at the Jade Palace. She is a master of the Tiger Style of kung fu."
                case "MONKEY":
                    collectible_metadata["description"] = "Master Monkey is one of the supporting characters of the Kung Fu Panda franchise. He is a member of the Furious Five as well as one of Master Shifu's students at the Jade Palace. He is a master of the Monkey Style of kung fu."
                case "CRANE":
                    collectible_metadata["description"] = "Master Crane is one of the supporting characters of the Kung Fu Panda franchise. He is a member of the Furious Five as well as one of Master Shifu's students at the Jade Palace. He is a master of the Crane Style of kung fu."
                case "MANTIS":
                    collectible_metadata["description"] = "Master Mantis is one of the supporting characters of the Kung Fu Panda franchise. He is a member of the Furious Five as well as one of Master Shifu's students at the Jade Palace. He is a master of the Mantis Style of kung fu."
                case "VIPER":
                    collectible_metadata["description"] = "Master Viper is one of the supporting characters of the Kung Fu Panda franchise. She is a member of the Furious Five and the daughter of Great Master Viper, as well as one of Master Shifu's students at the Jade Palace. She is a master of the Viper Style of kung fu."

            image_path = "./img/" + character.lower().replace("_", "-") + ".png"

            image_uri = None
            if os.getenv("UPLOAD_IPFS") == "true":
                image_uri = upload_to_ipfs(image_path)
            image_uri = image_uri if image_uri else character_to_image_uri[character]

            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            if os.getenv("UPLOAD_IPFS") == "true":
                upload_to_ipfs(metadata_file_name)


# curl -X POST -F file=@metadata/rinkeby/0-SHIBA_INU.json http://localhost:5001/api/v0/add


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-PUG.png" -> "0-PUG.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
