# get and set methods are uncommonly used in python

class Student:
    # self is the object being initialized
    def __init__(self, name, id, gpa): # Setting up class variables within the initializer method
        self.name = name # name is a variable of the Student object
        self.id = id     # id is a variable of the Student object
        self.gpa = gpa   # gpa is a variable of the Student object

    def __str__(self): # This method returns a string representation of the object
        return f'Student Name: {self.name}, Student ID: {self.id} Current GPA: {self.gpa}'


alex = Student('Alex', 'abcdef', 2.4) # Creating an instance of the Student class
print(alex.name) # Accessing the name variable of the alex object
print(alex.id) # Accessing the school_id variable of the alex object

print(alex) # This will call the __str__ method and print the string representation of the object

maya = Student('Maya', 'ghijkl', 4.0) # Creating another instance of the Student class
print(maya) # This will call the __str__ method and print the string representation of the object

jacob = Student('Jacob', 'mnopqr', 3.2) # Creating another instance of the Student class
print(jacob)
print(f'Jacobs Current GPA is: {jacob.gpa}') # Accessing the gpa variable of the jacob object

jacob.gpa = 3.5 # Modifying the gpa variable of the jacob object

print(f'Jacobs Updated GPA is: {jacob.gpa}')