import json
from product import Product

FILE_NAME = "stock.json"

def load_products():
    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)
            return [Product(item["model"], item["name"], item["quantity"]) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_products(products):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump([p.to_dict() for p in products], file, indent=4)
    except Exception as e:
        print("Error saving file:", e)