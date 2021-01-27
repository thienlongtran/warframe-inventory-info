import requests
import json

API = "https://api.warframe.market/v1/items/"

def getAveragePlatPrice(item_name):
    """
    Returns the average platinum market price of the item.
    """

    item_name = clean(item_name)
    item_info = requests.get(API + item_name.replace(" ", "_") + "/statistics").json()
    avg_price = item_info["payload"]["statistics_closed"]["48hours"][0]['avg_price']
    
    return avg_price

def clean(item_name):
    """
    Returns a cleaned version of the item name for use in API.
    """

    item_name = item_name.replace(" ", "_")
    item_name = item_name.lower()

    return item_name