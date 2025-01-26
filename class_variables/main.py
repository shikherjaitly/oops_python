class Student:

	class_year = 2024
	num_students = 0
	def __init__(self, name, age):
		self.name = name
		self.age = age
		Student.num_students += 1 
		#when referring to the class variable use the class name instead of self for clarity
		
student1 = Student("spongebob", 30)
student2 = Student("patrick", 35)
student3 = Student("squidward", 69)
student4 = Student("Sandy", 27)

# print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} Students")

print(f"{student1.name} is {student1.age} years old" )
print(f"{student2.name} is {student2.age} years old" )
print(f"{student3.name} is {student3.age} years old" )
print(f"{student4.name} is {student4.age} years old" )