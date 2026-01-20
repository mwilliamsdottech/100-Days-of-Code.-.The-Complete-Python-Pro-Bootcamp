capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested list in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],

# }

# Print Lille
# print(travel_log["Germany"][1])

# Nested list
# nested_list = ["A", "B", ["C", "D"]]

# Print the letter D inside the nested list
# print(nested_list[2][1])

# Nested Dictionary in Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
# print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])