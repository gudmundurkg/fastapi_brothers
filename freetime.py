from fastapi import FastAPI

app = FastAPI()

db = [
    {"id": 0, "name": "basketball", "location": "California", "locationLatLon": {"lat": 40.7128, "lon": -74.0060}, "opening_hours": "99-99"},
    {"id": 1, "name": "baseball", "location": "New York", "locationLatLon": {"lat": 40.7128, "lon": -74.0060}, "opening_hours": "99-99"},
    {"id": 2, "name": "soccer", "location": "Florida", "locationLatLon": {"lat": 40.7128, "lon": -74.0060}, "opening_hours": "99-99"},
    {"id": 3, "name": "tennis", "location": "Texas", "locationLatLon": {"lat": 40.7128, "lon": -74.0060}, "opening_hours": "99-99"},
    {"id": 4, "name": "swimming", "location": "Florida", "locationLatLon": {"lat": 40.7128, "lon": -74.0060}, "opening_hours": "99-99"},
    {"id": 5, "name": "The Great Movie Cinema", "location": "California", "locationLatLon": {"lat": 40.7128, "lon": -74.0060}, "opening_hours": "10-23"}
]

# http://127.0.0.1:8000/freetime
# http://127.0.0.1:8000/freetime?location=California
@app.get("/freetime")
def get_freetime(location: str|None = None, opening_hours: str|None = None):
    if location is not None:
        return [item for item in db if item["location"] == location]
    elif opening_hours == "all_day":
        return [item for item in db if item["opening_hours"] == "99-99"]
    else:
        return db

# http://127.0.0.1:8000/freetime/opening-hours?lower_opening=10&upper_opening=22
# http://127.0.0.1:8000/freetime/opening-hours?lower_opening=23&upper_opening=24 (should returns all day openings)
@app.get("/freetime/opening-hours")
def get_freetime_opening_hours(lower_opening: int|None = None, upper_opening: int|None = None) -> list:    
    if lower_opening is not None and upper_opening is not None:
        opening_hours = [item for item in db if int(item["opening_hours"].split("-")[0]) >= lower_opening and int(item["opening_hours"].split("-")[1]) <= upper_opening]
        all_day_openings = [item for item in db if item["opening_hours"] == "99-99"]
        return opening_hours + all_day_openings        
    else:
        return []

@app.get("/freetime/{id}")
def get_freetime_by_id(id: int):
    return db[id]