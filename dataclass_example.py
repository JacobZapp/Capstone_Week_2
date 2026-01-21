from dataclasses import dataclass

@dataclass

class Student:
    name: str
    id: str
    gpa: float

    def __str__(self):
        return f'Student Name: {self.name}, Student ID: {self.id} Current GPA: {self.gpa}'

# main function to demonstrate usage and adding students and printing their information as needed
def main():
    jacob = Student('Jacob', 'mnopqr', 3.2) # Creating another instance of the Student class
    print(jacob)
    print(jacob.name)
    print(jacob.id)
    print(jacob.gpa)

    maya = Student('Maya', 'ghijkl', 4.0) # Creating another instance of the Student class
    print(maya)

# this is checking if its being run from CMD or imported, __name__ is a special variable in python, we will learn more
if __name__ == '__main__':
    main()