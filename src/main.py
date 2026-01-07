airports = {
    "JFK": {
        "name": "John F Kennedy International",
        "liverpool_distance": 5326,
        "bournemouth_distance": 5486
    },
    "ORY": {
        "name": "Paris-Orly",
        "liverpool_distance": 629,
        "bournemouth_distance": 379
    },
    "MAD": {
        "name": "Adolfo Suarez Madrid-Barajas",
        "liverpool_distance": 1428,
        "bournemouth_distance": 1151
    },
    "AMS": {
        "name": "Amsterdam Schiphol",
        "liverpool_distance": 526,
        "bournemouth_distance": 489
    },
    "CAI": {
        "name": "Cairo International",
        "liverpool_distance": 3379,
        "bournemouth_distance": 3584
    },
}

aircrafts = {
    "Medium narrow body": {
        "running_cost": 8,
        "range": 2650,
        "standard_capacity": 180,
        "min_first_class": 8
    },
    "Large narrow body": {
        "running_cost": 7,
        "range": 5600,
        "standard_capacity": 220,
        "min_first_class": 10
    },
    "Medium wide body": {
        "running_cost": 5,
        "range": 4050,
        "standard_capacity": 406,
        "min_first_class": 14
    }
}

def enter_airport_code(prompt):
    codes = []
    for airport in airports:
        codes.append(airport["code"].upper())
    code = ""
    code = input(prompt).upper()
    while code not in codes:#
        print("Please enter a valid airport code.")
        code = input(prompt).upper()
    return code

uk_airport = enter_airport_code("Enter the code for the UK airport: ")
overseas_airport = enter_airport_code("Enter the code for the international airport: ")

