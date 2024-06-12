class Character:
	def __init__(self,name,weapon):
		self.name = name
		self.weapon = weapon

	def attack(self):
		pass
	
# Students can have different names and function bodies for classes

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

# Students can have different names for instances.

mario = Soldier("Mario", "Cart")
mario.attack()

turtle = Ninja("Turtle", "Sword")
turtle.attack()

harryPotter = Wizard("Harry Potter", "Magic Spell")
harryPotter.attack()

griffin = Dragon("Griffin", "Tail")
griffin.attack()