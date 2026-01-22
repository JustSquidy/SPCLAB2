class Student:
    def __init__(self, name, school_id, gpa):
        self.name = name
        self.school_id = school_id
        self.gpa = gpa

    def __str__(self):
        return f'Student Name: {self.name}, School ID: {self.school_id} Current GPA: {self.gpa}'
        

alex = Student('Alex', 'ABCDEF', 3.5)
print(alex.name) # shows name Alex
print(alex.school_id) # shows id  ABCDEF
print(alex) # uses __str__ method to print student details

sam = Student('Sam', 'GHIJKL', 3.8)
print(sam) # shows name Sam