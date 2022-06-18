from fastapi import FastAPI

app = FastAPI()

db = [
    {"id": 0, "name": "The House of Kobe", "location": "Los Angeles, CA", "price": "$$$", "take_away": "false", "delivery": "false" },
    {"id": 1, "name": "The House of Pasta", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false" },
    {"id": 2, "name": "The House of Bagels", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false" },
    {"id": 3, "name": "The House of Pizzas", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false" },
    {"id": 4, "name": "The House of Burgers", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false" },
    {"id": 5, "name": "The House of Tacos", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false" },
    {"id": 6, "name": "The House of Sushi", "location": "1123 Main St, Anytown, CA 12345", "price": "$$$", "take_away": "false", "delivery": "false" },
    {"id": 7, "name": "The House of Steak", "location": "1123 Main St, Anytown, CA 12345", "price": "$$$", "take_away": "false", "delivery": "false" },
    {"id": 8, "name": "Dominos", "location": "Los Angeles, CA", "price": "$", "take_away": "true", "delivery": "true"},
    {"id": 9, "name": "Pizza Hut", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true"},
    {"id": 10, "name": "Subway", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true"},
    {"id": 11, "name": "McDonalds", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true"},
    {"id": 12, "name": "KFC", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true"},
    {"id": 13, "name": "Taco Bell", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true"},
    {"id": 14, "name": "Wendy's", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "true", "delivery": "true"},
    {"id": 15, "name": "Burger King", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "true", "delivery": "true"},
]

@app.get("/food/")
def get_food():
    return db

@app.get("/food/{id}")
def get_food_by_id(id: int):
    return db[id]

@app.get("/food/name/{name}")
def get_food_by_name(name: str):
    return db[id][name]

@app.get("/food/location/{location}")
def get_food_by_location(location: str):
    return db[id][location]

@app.get("/food/take_away/{take_away}")
def get_food_by_take_away(take_away: str):
    return db[id][take_away]

@app.get("/food/delivery/{delivery}")
def get_food_by_delivery(delivery: str):
    return db[id][delivery]

@app.get("/food/{id}/price-range")
def get_food_by_id_with_price_range(id: int, lower_price: str|None = None, upper_price: str|None = None):
    if lower_price is not None and upper_price is not None:
        return [d for d in db if d["price"] >= lower_price and d["price"] <= upper_price]
    else:
        return []