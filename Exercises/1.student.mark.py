# Practical work 1: student mark management
# • Make a new Python program
# • Name it «1.student.mark.py»
# • Use tuples, dicts, lists, NO objects/classes
# • Build a student mark management system
# 1.student.mark.py

students = []
courses = []
marks = {}
num_students = int(input("Enter number of students: "))

for i in range(num_students):
    sid = input("Student ID: ")
    name = input("Student name: ")
    dob = input("Date of birth: ")
    students.append((sid, name, dob))  

num_courses = int(input("\nEnter number of courses: "))

for i in range(num_courses):
    cid = input("Course ID: ")
    cname = input("Course name: ")
    courses.append((cid, cname))

print("\n--- Student List ---")
for s in students:
    print(s)

print("\n--- Course List ---")
for c in courses:
    print(c)

selected_course = input("\nEnter course ID to input marks: ")
marks[selected_course] = {}

for s in students:
    mark = float(input(f"Mark for {s[1]} (ID: {s[0]}): "))
    marks[selected_course][s[0]] = mark


print("\n--- Marks in Course", selected_course, "---")
for sid, mark in marks[selected_course].items():
    print("Student ID:", sid, "| Mark:", mark)
