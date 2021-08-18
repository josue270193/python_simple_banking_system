class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the student_id here
        self.student_id = f"{name[0]}{last_name}{birth_year}"


student_name = input()
student_last_name = input()
student_birth_year = int(input())
student = Student(student_name, student_last_name, student_birth_year)
print(student.student_id)
