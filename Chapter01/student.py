class Student:
    active = True

    def __init__(self,name,credits):  # constructor
        self.name = name
        self.credits = credits
    
    def get_name(self):
        return self.name
    
    def get_credits(self):
        if self.active:
            return self.credits
        else:
            return 0
    
    def get_active(self):
        return self.active
    
    def change_name(self,new_name):
        self.name = new_name
    
    def change_credits(self,new_credits):
        self.credits = new_credits
    
    def change_active(self,new_active):
       self.active = new_active

def test_student():
    s1 = Student("Tony Stark",160)
    assert s1.get_name()=="Tony Stark", "Student: test 0 failed"
    assert s1.get_credits()==160, "Student: test 1 failed"
    assert s1.get_active()==True, "Student: test 2 failed"

    s2 = Student("Bruce Banner",154)
    assert s2.get_name()=="Bruce Banner", "Student: test 3 failed"
    assert s2.get_credits()==154, "Student: test 4 failed"
    assert s2.get_active()==True, "Student: test 5 failed"

    s1.change_name("Ironman")
    assert s1.get_name()=="Ironman", "Student: test 6 failed"

    s2.change_credits(158)
    assert s2.get_credits()==158, "Student: test 7 failed"

    s1.change_active(False)
    assert s1.get_active()==False, "Student: test 8 failed"
    assert s1.get_credits()==0, "Student: test 9 failed" # since s1 is inactive now

test_student()

