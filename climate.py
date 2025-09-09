# people.py

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

CLIMATE = {
    "cstat 23": {
        "station": 23,
        "temp": 8.4,
        "humid": 60.4,
        "timestamp": get_timestamp(),
    },
    "cstat 25": {
        "station": 25,
        "temp": 9.2,
        "humid": 62.4,
        "timestamp": get_timestamp(),
    },
    "cstat 26": {
        "station": 26,
        "temp": 6.3,
        "humid": 65.1,
        "timestamp": get_timestamp(),
    }
}

def read_all():
    return list(CLIMATE.values())

def delete_all():
    global CLIMATE
    saved_climate = CLIMATE
    CLIMATE = {}
    return list(saved_climate.values())

def register(climateData):
    station = climateData.get("station")
    station_name = f"cstat {station}"
    temp = climateData.get("temp")
    humid = climateData.get("humid")
    CLIMATE[station_name] = {
        "temp": float(temp),
        "humid": float(humid),
        "station": int(station),
        "timestamp": get_timestamp(),
    }
    return CLIMATE[station_name], 201
