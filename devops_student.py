from student_data import Student


class Devops(Student):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)



s = Student("Ib", "Bocus")
d = Devops("Ib", "Bocus")

s.full_name()
s.roll_call()
d.full_name()
d.roll_call()