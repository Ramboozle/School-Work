#A206 CLASSES CONCEPTS DEMO
#Create code that demonstrates the use of classes, inheritance, polymorphism and containment (aggregation)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
