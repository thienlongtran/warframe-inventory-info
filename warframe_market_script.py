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
    Returns the average platinum market price of the item.
    """

    avg_price = 0
    item_name = clean(item_name)
    item_info = requests.get(API + item_name.replace(" ", "_") + "/statistics").json()
    
    try: 
        avg_price = item_info["payload"]["statistics_closed"]["48hours"][0]['avg_price']

    except KeyError:
        print(item_name + " is not a valid item.")
    
    return avg_price

def clean(item_name):
    """
    Returns a cleaned version of the item name for use in API.
    """
    if item_name.split()[0] in warframes_list and item_name.split()[len(item_name.split())-2] != "Prime" and item_name.split()[len(item_name.split())-1] == "Blueprint":
        item_name = item_name.replace(" Blueprint", "")

    item_name = item_name.replace(" ", "_")
    item_name = item_name.lower()

    return item_name