players = [
    {
        "name": "Messi",
        "nationalTeam": "Argentina",
        "club": "Barcelona",
        "age": 32
    },
    {
        "name": "Ronaldo",
        "nationalTeam": "Portugal",
        "club": "Juventus",
        "age": 35
    },

]

def FindPlayer(name):
    for player in players:
        if (player['name'].lower() == name.lower()):
            return str(player)    
    return str({"message": "invalid name " + name})

