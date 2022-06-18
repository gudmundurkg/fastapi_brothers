from fastapi import FastAPI

app = FastAPI()

db = [
    {"id": 0, "name": "The House of Kobe", "location": "Los Angeles, CA", "price": "$$$", "take_away": "false", "delivery": "false", "opening_hours": "10-22" },
    {"id": 1, "name": "The House of Pasta", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false", "opening_hours": "10-22" },
    {"id": 2, "name": "The House of Bagels", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false", "opening_hours": "10-22" },
    {"id": 3, "name": "The House of Pizzas", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false", "opening_hours": "11-20" },
    {"id": 4, "name": "The House of Burgers", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false", "opening_hours": "10-19" },
    {"id": 5, "name": "The House of Tacos", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "false", "delivery": "false", "opening_hours": "10-22" },
    {"id": 6, "name": "The House of Sushi", "location": "1123 Main St, Anytown, CA 12345", "price": "$$$", "take_away": "false", "delivery": "false", "opening_hours": "10-22" },
    {"id": 7, "name": "The House of Steak", "location": "1123 Main St, Anytown, CA 12345", "price": "$$$", "take_away": "false", "delivery": "false", "opening_hours": "10-22" },
    {"id": 8, "name": "Dominos", "location": "Los Angeles, CA", "price": "$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
    {"id": 9, "name": "Pizza Hut", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
    {"id": 10, "name": "Subway", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
    {"id": 11, "name": "McDonalds", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
    {"id": 12, "name": "KFC", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
    {"id": 13, "name": "Taco Bell", "location": "1123 Main St, Anytown, CA 12345", "price": "$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
    {"id": 14, "name": "Wendy's", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
    {"id": 15, "name": "Burger King", "location": "1123 Main St, Anytown, CA 12345", "price": "$$", "take_away": "true", "delivery": "true", "opening_hours": "10-22" },
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

@app.get("/food/price/{price}")
def get_food_by_price(price: str):
    return db[id][price]

# http://127.0.0.1:8000/food/all/price-range?lower_price=$$
# http://127.0.0.1:8000/food/all/price-range?lower_price=$$&upper_price=$$$
@app.get("/food/all/price-range")
def get_food_by_id_with_price_range(lower_price: str|None = None, upper_price: str|None = None, flexible: str|None = None):
    if lower_price is not None and upper_price is not None:
        return [d for d in db if d["price"] >= lower_price and d["price"] <= upper_price]
    elif lower_price is not None and flexible is True:
        return [d for d in db if d["price"] >= lower_price]
    elif upper_price is not None and flexible is True:
        return [d for d in db if d["price"] <= upper_price]
    else:
        return []

# http://127.0.0.1:8000/food/all/opening-hours?lower_opening=10&upper_opening=22&flexible=true
# http://127.0.0.1:8000/food/all/opening-hours?lower_opening=10&upper_opening=22
# http://127.0.0.1:8000/food/all/opening-hours?lower_opening=10
# http://127.0.0.1:8000/food/all/opening-hours?upper_opening=22
@app.get("/food/all/opening-hours")
def get_food_with_opening_hours(lower_opening: int|None = None, upper_opening: int|None = None, flexible: bool|None = None) -> list:    
    if lower_opening is not None and upper_opening is not None and flexible is True:        
        return [d for d in db if int(d["opening_hours"].split("-")[0]) <= lower_opening + 2 and int(d["opening_hours"].split("-")[1]) >= upper_opening - 2]
    elif lower_opening is not None and upper_opening is not None:              
        return [d for d in db if int(d["opening_hours"].split("-")[0]) <= lower_opening and int(d["opening_hours"].split("-")[1]) >= upper_opening]
    elif lower_opening is not None:
        return [d for d in db if int(d["opening_hours"].split("-")[0]) <= lower_opening]
    elif upper_opening is not None:
        return [d for d in db if int(d["opening_hours"].split("-")[1]) >= upper_opening]     
    else:        
        return []