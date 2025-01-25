from car import Car

car1 = Car("kylaq", 2024, "red", True)
car2 = Car("kushaq", 2022, "brown", True)
car3 = Car("BE 6", 2024, "red", True)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.drive()
car2.drive()

car1.describe()