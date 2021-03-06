import requests
import json

API = "https://api.warframe.market/v1/items/"

warframes_list = ["Ash" , "Atlas" , "Banshee" , "Baruuk" , "Chroma" , "Ember" , "Equinox" ,
"Excalibur" , "Frost" , "Gara" , "Garuda" , "Gauss" , "Grendel" , "Harrow" , "Hildryn" , "Hydroid" ,
"Inaros" , "Ivara" , "Khora" , "Lavos" , "Limbo" , "Loki" , "Mag" , "Mesa" , "Mirage" , "Nekros" ,
"Nezha" , "Nidus" , "Nova" , "Nyx" , "Oberon" , "Octavia" , "Protea" , "Revenant" , "Rhino" , "Saryn" ,
"Titania" , "Trinity" , "Valkyr" , "Vauban" , "Volt" , "Wisp" , "Wukong" , "Xaku" , "Zephyr"]

def getAveragePlatPrice(item_name):
    """
    Get the current average price of the item on the Warframe marketplace.

    Args:
        item_name (str): The name of the item.

    Returns:
        float: the average platinum market price of the item.
    """

    avg_price = -1
    item_name = clean(item_name)
    item_info = requests.get(API + item_name.replace(" ", "_") + "/statistics").json()
    
    try: 
        avg_price = item_info["payload"]["statistics_closed"]["48hours"][0]['avg_price']

    except KeyError:
        print(item_name + " is not listed on warframe.market.")
    
    return avg_price

def getDucatPrice(item_name):
    """
    Get the current Ducat price of the item for Baro Ki'Teer ingame trading.

    Args:
        item_name (str): The name of the item.

    Returns:
        float: The ducat price of the item.
    """

    ducat_price = -1
    item_name = clean(item_name).title().replace("_", " ")

    #List of the Ducat values as JSON.
    #Credit: Jonathan Sourdough (https://github.com/JonathanSourdough)
    ducat_list = requests.get("https://s3.us-east-2.amazonaws.com/www.jsourdough.com/ItemsAndDucats.json").json()

    try: 
        ducat_price = ducat_list["itemsDucat"][item_name]

    except KeyError:
        print(item_name + " does not have a ducat value.")

    return ducat_price

def clean(item_name):
    """
    Convert the name of the item into one that's usable for the warframe.market API

    Args:
        item_name (str): The name of the item.

    Returns:
        str: A cleaned version of the item name usable with the warframe.market API.
    """
    if item_name.split()[0] in warframes_list and item_name.split()[len(item_name.split())-2] != "Prime" and item_name.split()[len(item_name.split())-1] == "Blueprint":
        item_name = item_name.replace(" Blueprint", "")

    item_name = item_name.replace(" ", "_")
    item_name = item_name.lower()

    return item_name