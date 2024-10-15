# class of Students and Teacherss
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"


# Student class
class Student(Person):
    def __init__(self, name, age, email, student_id, major):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.major = major
        self.grades = {}

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def get_grades(self):
        return self.grades

    def get_details(self):
        details = super().get_details()
        return f"{details}, Student ID: {self.student_id}, Major: {self.major}"


# Teacher class
class Teacher(Person):
    def __init__(self, name, age, email, employee_id, department):
        super().__init__(name, age, email)
        self.employee_id = employee_id
        self.department = department
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def get_courses(self):
        return self.courses

    def get_details(self):
        details = super().get_details()
        return f"{details}, Employee ID: {self.employee_id}, Department: {self.department}"


# University class to manage Students and Teachers
class University:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_all_students(self):
        return [student.get_details() for student in self.students]

    def get_all_teachers(self):
        return [teacher.get_details() for teacher in self.teachers]

    def get_university_info(self):
        return f"University: {self.name}, Total Students: {len(self.students)}, Total Teachers: {len(self.teachers)}"


# Creating the University
uni = University("NTU University")

# Adding Students
student1 = Student("Ali", 20, "ali@example.com", "S12345", "Computer Science")
student2 = Student("Saad", 22, "saad@example.com", "S12346", "Mathematics")
uni.add_student(student1)
uni.add_student(student2)

# Adding Teachers
teacher1 = Teacher("Irshad", 45, "irshad@example.com", "T98765", "Computer Science")
teacher2 = Teacher("Ahmed", 50, "ahmed@example.com", "T98766", "Mathematics")
uni.add_teacher(teacher1)
uni.add_teacher(teacher2)

# Assign courses to teachers
teacher1.assign_course("BS Textlie Management & Marketing")
teacher2.assign_course("BS Comuter Science")

# Add grades for students
student1.add_grade("BS Textlie Management & Marketing", "A")
student2.add_grade("BS Comuter Science", "B")

# Output
print(uni.get_university_info())
print("\nStudents:")
for student_details in uni.get_all_students():
    print(student_details)

print("\nTeachers:")
for teacher_details in uni.get_all_teachers():
    print(teacher_details)

print("\nCourses taught by Irshad:", teacher1.get_courses())
print("Grades for Ali:", student1.get_grades())
