class Student:
    """
    A Student has the following characteristics:
    - name (nonempty string)
    - age (positive int)
    - gpa (float in the range [0.0, 4.0])

    A Student has the following methods:
    - get_name() -> str: Returns the name of the student.
    - get_age()  -> int: Returns the age of the student.
    - get_gpa()  -> float: Returns the GPA of the student.
    - set_name(name): Sets the name of the student.
    - set_age(age):   Sets the age of the student.
    - set_gpa(gpa):   Sets the GPA of the student.
    """
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gpa(self):
        return self.gpa    
    
    def set_name(self,name):
        self.name = name

    def set_age(self, age):
        self.age = age
    
    def set_gpa(self, gpa):
        self.gpa = gpa

"""
Write a function to test the Student class.
"""
def test_Student():
    """
    Signature: () -> None
    Purpose: Tests the Student class.
    Design Idea: Test the constructor, getters, and setters for two students.
    """
    student1 = Student("Marcelina", 23, 3.9)
    student2 = Student("Mandrake", 18, 1.7)

    assert student1.get_name() == "Marcelina", "Test Case 0 Failed"
    assert student1.get_age() == 23, "Test Case 1 Failed"
    assert student1.get_gpa() == 3.9, "Test Case 2 Failed"

    assert student2.get_name() == "Mandrake", "Test Case 3 Failed"
    assert student2.get_age() == 18, "Test Case 4 Failed"
    assert student2.get_gpa() == 1.7, "Test Case 5 Failed"

    student1.set_name("Oliwia")
    student1.set_gpa(4.0)
    assert student1.get_name() == "Oliwia", "Test Case 6 Failed"
    assert student1.get_gpa() == 4.0, "Test Case 7 Failed"
    assert student2.get_name() == "Mandrake", "Test Case 8 Failed"
    assert student2.get_gpa() == 1.7, "Test Case 9 Failed"
    student2.set_age(19)
    assert student2.get_age() == 19, "Test Case 10 Failed"
    assert student1.get_age() == 23, "Test Case 11 Failed"

test_Student()

"""
Template for functions on a Student.

def function_name(a_student ...):
    Signature: Student ... -> return_type
    Purpose: 
    Design Idea:

    Useful expressions:
        a_student.get_name()
        a_student.get_age()
        a_student.get_gpa()
        a_student.set_name(name)
        a_student.set_age(age)
        a_student.set_gpa(gpa)
    return ...

def test_function_name():
    Signature: () -> None
    Purpose: 
    Design Idea:

    student1 = Student("Tiksi", 23, 3.9)
    student2 = Student("Bob", 18, 1.7)
         .
         .
         .
    assert function_name(student1, ...) == , "Test Case 0 Failed"
    assert function_name(student2, ...) == , "Test Case 1 Failed"
         .
         .
         .

test_function_name()
"""
    

def is_on_Dean_list(a_student):
    """
    Signature: Student -> bool
    Purpose: Determines if a student is on the Dean's list.
    Design Idea: A student is on the Dean's list if their GPA 
                 is 3.6 or higher.
    """
    return a_student.get_gpa() >= 3.6

"""
Define a test for is_on_Dean_list
"""
def test_is_on_Dean_list():
    """
    Signature: () -> None
    Purpose: Tests the is_on_Dean_list function.
    Design Idea: Test 6 students with different GPAs.
                 Some with gpa >= 3.6, others with gpa < 3.6,
                 and some with gpa == 3.6.
    """
    student1 = Student("Tiksi", 23, 3.9)
    student2 = Student("Bob", 18, 1.7)
    student3 = Student("David", 21, 3.6)
    student4 = Student("Chuck", 22, 3.0)
    student5 = Student("Gina", 18, 3.67)
    student6 = Student("Andres", 23, 3.6)

    assert is_on_Dean_list(student1) == True, "Test Case 0 Failed"
    assert is_on_Dean_list(student2) == False, "Test Case 1 Failed"
    assert is_on_Dean_list(student3) == True, "Test Case 2 Failed"
    assert is_on_Dean_list(student4) == False, "Test Case 3 Failed"
    assert is_on_Dean_list(student5) == True, "Test Case 4 Failed"
    assert is_on_Dean_list(student6) == True, "Test Case 5 Failed"

test_is_on_Dean_list()


