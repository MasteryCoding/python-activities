# Title

## Introduction

## Overview

### Step 1: My Favorite Video Game Characters Dictionary

In this activity we're going to get some practice working with sets and dictionaries. The first thing we'll do is create a new dictionary to store some information, specifically some information about some of our favorite video game characters. If you're not interested in video game characters that's not a problem! You can do this activity with all kinds of characters. Maybe you use baseball players, soccer players, or even your favorite characters from TV shows.

Here's an example below. Dictionaries store key-value pairs.

##### Question: In the dictionary below, what `type` are the `keys` and what `type` are the `values`?

```py
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
```

#### Test Code

To test this code and make sure you have the dictionary set up correctly you can try running code like this to print values from the dictionary.

```py
print(favorite_characters['Link']['game']) # print the game that link comes from
```

#### Solution

Just for teachers for now - solution code for this step.

### Step 2: Name Set

In this step we'll collect some information about our favorite characters. Let's create a new python variable called `name_set` with the type `set` that we'll use to store the names of our favorite characters.

- To create a new set use the `set()` method like so:
```py
name_set = set() # creates an empty set
```
- Iterate through the dictionary adding the names of each character to the name set.
#### Hint: Iterate through a dictionary similar to how you would a list.
```py
for key in my_dictionary:
    print(key)
```
- Use the starter code below as a starting point.

```py
def make_name_set(characters):
    # declare name set 
    # iterate through characters in name set and add each character's name to the name set. 
    # return the name set
```

#### Test Code

To test your code you can iterate through values in the name set and print them out like so:

```py
name_set = make_name_set(favorite_characters)
for name in name_set:
    print(name)
```

If everything went according to plan you should see the output of each of the characters in your dictionary:

```
Link
Mario
Master Chief
Geralt of Rivia
```

#### Solution

```py
def make_name_set(characters):
    # declare name set 
    name_set = set()
    # iterate through characters in name set and add each character's name to the name set. 
    for character in characters:
        name_set.add(character)
    # return the name set
    return name_set
```

### Step 3: Game Set

In this next set we'll collect the games (or some other value if you're using different types of characters) that each of our characters come from.

However, this function will be a little different. In the previous step the names were the keys in our top level dictionary, but now we need to find the game key for each character. This should look like this:

```py
print(favorite_characters['Link']['game']) # get the game that link comes from 
```

Or if you're iterating through the characters dictionary you can use the key from the loop like so:
```py
for key in favorite_characters:
    # key is their name in this case
    print(favorite_characters[key]['game'])
```

For this last step we'll create a set of all the games these characters appear of in a similar function. You can use the starter code below to get started.

```py
def make_game_set(characters):
    # - declare game_set
    # - iterate through characters by name
    # - for each character get the game parameter and add the value to 
    #   the game set
    # - return the game set

```

#### Test Code

```py
game_set = make_game_set(favorite_characters)
for game in game_set:
    print(game)
```

My output looks like this
```
Halo: Combat Evolved
The Legend of Zelda
Super Mario Bros.
The Witcher 3: Wild Hunt
```


#### Solution

```py
def make_game_set(characters):
    game_set = set()
    for name in characters:
        game_set.add(characters[name]['game'])
    return game_set
```

## Conclusion