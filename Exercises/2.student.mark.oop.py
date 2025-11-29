# • Copy your practical work 1 to 2.student.mark.oop.py
# • Make it OOP’ed
# • Same functions
# • Proper attributes and methods
# • Proper encapsulation
# • Proper polymorphism
# • e.g. .input(), .list() methods



class Student:
    
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def get_students(self):
        return self.__students
    def get_courses(self):
        return self.__courses
    def get_marks(self):
        return self.__marks
    def set_students(self, students):
        self.__students = students
    def set_courses(self, courses):
        self.__courses = courses
    def set_marks(self, marks):
        self.__marks = marks
    
    def input(self):
        num_students = int(input("Enter number of students: "))
        for _ in range(num_students):
            sid = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Date of birth: ")
            self.__students.append((sid, name, dob))  
        num_courses = int(input("\nEnter number of courses: "))

        for _ in range(num_courses):
            cid = input("Course ID: ")
            cname = input("Course name: ")
            self.__courses.append((cid, cname))
    
    def output(self):
        print("\n--- Student List ---")
        for s in self.__students:
            print(s)

        print("\n--- Course List ---")
        for c in self.__courses:
            print(c)

        selected_course = input("\nEnter course ID to input marks: ")
        self.__marks[selected_course] = {}

        for s in self.__students:
            mark = float(input(f"Mark for {s[1]} (ID: {s[0]}): "))
            self.__marks[selected_course][s[0]] = mark


        print("\n--- Marks in Course", selected_course, "---")
        for sid, mark in self.__marks[selected_course].items():
            print("Student ID:", sid, "| Mark:", mark)

        
manage = Student()
manage.input()
manage.output()
        
        

        
        
