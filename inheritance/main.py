class Animal:
	def __init__(self, name):
		self.name = name
		self.is_alive = True
		
	def eat(self):
		print(f"{self.name} is eating")
	
	def sleep(self):
		print(f"{self.name} is sleeping")
		
class Dog(Animal):
	def speak(self):
		print("Woof!")
	
class Cat(Animal):
	def speak(self):
		print("Meow!")

class Mouse(Animal):
	def speak(self):
		print("Squeak!")
	
dog = Dog("Ellie")
cat = Cat("garfeild")
mouse = Mouse("mooshak")


print(f"{dog.name} is a dog")
print(f"{cat.name} is a cat")
print(f"{mouse.name} is a mouse")

mouse.speak()
dog.speak()
cat.speak()