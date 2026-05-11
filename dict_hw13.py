car_info = {
    "model": "Toyota Hilux",
    "price, UAH": 2107250,
    "displacement, cm^3": 2393,
    "weight, kg": 2175,
    "top speed, kph": 170,
    "fuel consumption per 100 km, l": 10.7,
    "interior": ["heated mirrors", "remote controlled central lock", "multi-information display"],
    "luggage compartment dimensions": {
        "length, mm": 1569,
        "width, mm": 1645,
        "height, mm": 481
    }
}
car_info["max towing capacity"] =  3500
car_model = car_info["model"]
car_price = car_info["price, UAH"]
first_option = car_info["interior"][0]
luggage_compartment_volume = (car_info["luggage compartment dimensions"]["length, mm"] *
                              car_info["luggage compartment dimensions"]["width, mm"] *
                              car_info["luggage compartment dimensions"]["height, mm"])
insurance = car_info["price, UAH"] * 0.005
car_info["insurance"] =  insurance
cost_per_200_km = car_info["fuel consumption per 100 km, l"] * 2 * 93
print(round(cost_per_200_km))