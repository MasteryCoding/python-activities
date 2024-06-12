# Game Character Generator 

## Introduction

In this activity, let’s imagine that we are asked to write a program that generates different game characters for a video game company. The company asks us to have 4 types of game characters with different names, weapons, and attack phrase. 

## Overview

### Step 1: Character Class

We will start with writing a parent class called `Character` that will become a layout for 4 different types of game characters. `Character` will always have the data for Name and Weapon and the function for Attack. 


Let’s begin with the starter code below: 
```py
# create class 
# create the data each character should have 
# create the function each character should have 

# hints: 
# use init to define data 
# use 'self' to refer data to its instance
# use 'pass' to skip defining the function body as this class is just a layout   
```

#### Solution

```py
class Character:
	def __init__(self,name,weapon):
		self.name = name
		self.weapon = weapon

	def attack(self):
		pass
```

### Step 2: Classes for 4 Types 

Now we will write 4 classes for different character types. 
Choose whatever name you want for these classes. All you have to make sure is that your classes should:

* Inherit `Character` class
* Have `attack` function printing out a phrase using the name and weapon of its instance

Here is the starter code you can begin with: 
```py
# create 4 Classes
# inherit Character class
# Define attack function using data of its instance

#hints:
#Use parenthesis for inheritance 
#Use f-string to include data for phrase in attack function

```

#### Solution

```py
class Soldier(Character):
	def attack(self):
		print(f"Roger; Soldier {self.name} under mission using {self.weapon}!")

class Ninja(Character):
	def attack(self):
		print(f"Swish! Ninja {self.name} secretly attacks with {self.weapon}!")

class Wizard(Character):
	def attack(self):
		print(f"Poof! Wizard {self.name} uses magical power with {self.weapon}!")

class Dragon(Character):
	def attack(self):
		print(f"Grrrr... Dragon {self.name} furiously fights with {self.weapon}!")
```
(Students can have different names and function bodies for classes.)

### Step 3: Creating an instance

All we have left is to test our classes by creating instances. 
Try creating instances of all 4 character types and call the `attack` function for each of them.  

#### Solution

```py
mario = Soldier("Mario", "Cart")
mario.attack()

turtle = Ninja("Turtle", "Sword")
turtle.attack()

harryPotter = Wizard("Harry Potter", "Magic Spell")
harryPotter.attack()

griffin = Dragon("Griffin", "Tail")
griffin.attack()
```
(Students can have different names for instances.)

## Conclusion

Woohoo! The video game company is very satisfied with our game character generator. 
Try out adding more data and functions to your class and creating more instances. 
