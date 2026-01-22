from dataclasses import dataclass

# - Python automatically creates __init__ and __str__ (but we overwrote it) Traditional classes require you to write those yourself


@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

    def __str__(self):
        return f'Student Name: {self.name}, School ID: {self.school_id} Current GPA: {self.gpa}'

def main():
    alex = Student('Alex', 'ABCDEF', 3.5)
    print(alex.name) # shows name Alex
    print(alex.school_id) # shows id  ABCDEF
    print(alex) # uses __str__ method to print student details

    sam = Student('Sam', 'GHIJKL', 3.8)
    print(sam) # shows sams details

    Javier = Student('Javier', 'MNOPQR', 3.6)
    print(Javier)

if __name__ == "__main__":
    main()