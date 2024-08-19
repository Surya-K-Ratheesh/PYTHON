names = []

with open("names.csv") as file:
    for line in file:
        name, country = line.rstrip().split(",")
        """
        player = {} #Empty dictionary
        player["name"] = name
        player["country"] = country
        """
        
        player = {"name" : name, "country" : country}
        names.append(player)


# This functions are used to get only the names/country from the dictionary........ Which is for sorting it in ascending or descending order.         
"""
def get_name(player):
    return player["name"]

def get_country(player):
    return player["country"]
        
for player in sorted(names, key=get_country, reverse = True):
    print(f"{player['name']} is from {player['country']}")
"""

# The above lines of code can be shortened by using the "lambda" function.

for player in sorted(names, key=lambda player : player["name"]):
    print(f"{player['name']} is from {player['country']}")