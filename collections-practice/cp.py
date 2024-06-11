favorite_characters = {
    "Mario": {
        "game": "Super Mario Bros.",
        "genre": "Platformer",
        "year_released": 1985,
        "publisher": "Nintendo"
    },
    "Link": {
        "game": "The Legend of Zelda",
        "genre": "Action-Adventure",
        "year_released": 1986,
        "publisher": "Nintendo"
    },
    "Master Chief": {
        "game": "Halo: Combat Evolved",
        "genre": "First-Person Shooter",
        "year_released": 2001,
        "publisher": "Microsoft Game Studios"
    },
    "Geralt of Rivia": {
        "game": "The Witcher 3: Wild Hunt",
        "genre": "Action RPG",
        "year_released": 2015,
        "publisher": "CD Projekt"
    }
}

def make_name_set(characters):
    # declare name set 
    name_set = set()
    # iterate through characters in name set and add each character's name to the name set. 
    for character in characters:
        name_set.add(character)
    # return the name set
    return name_set

def make_game_set(characters):
    game_set = set()
    for name in characters:
        game_set.add(characters[name]['game'])
    return game_set
