# Imagine You run an Institute where all your students are stored in a variable something like this :
# students = 'david mark bill sam'
# You have a few tasks to do like :
# 1- Add a student given by user
# 2- Delete a student given by user
# 3- Find a student given by user
# 4- Replace a Student

# 1- Add a student given by user
students = 'david mark bill sam'
new_student = input("Enter the name:")
students_list = students.split()
students_list.append(new_student)
#print(students_list)
final_students_list = " ".join(students_list)
print("List of students after adding students by the user:", final_students_list)

# 2- Delete a student given by user:-
name = input("Enter the name:")
list_after_deleting_student_name = students.replace(name,"")
print("List of students after deleting the student name by the user:", list_after_deleting_student_name )

# 3- Find a student given by user:-
name = input("Enter the name:")
if name in students:
    print("True")
else:
    print("False")

# 4- Replace a Student:-
old_name= input("Enter the old student name:")
new_name = input("Enter the new student name:")
new_list_of_student= students.replace(old_name, new_name)
print("The new list after replace the old student name:", new_list_of_student)