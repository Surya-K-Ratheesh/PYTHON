players = [
    {"name" : "Cristiano", "last_name" : "Ronaldo" , "country" : "Portugal"},       # KEY - name. lastname , country    VALUE - Cristiano, Ronaldo, Portugal
    {"name" : "Lionel", "last_name" : "Messi" , "country" : "Argentina"},
    {"name" : "Neymar", "last_name" : "JR" , "country" : "Brazil"},
    {"name" : None, "last_name" : None , "country" : None} # Keyword - None
]

for player in players:
    print(player["name"], player["last_name"], "," , player["country"])