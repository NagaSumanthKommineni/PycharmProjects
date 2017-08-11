
students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def print_student_details():
    print("The Student list is :")
    for student in students:
        for key,value in student.items():
            print("\t",key,":",value)


def add_student(name,studentid=777):
    student = {"name":name,"studentid":studentid}
    students.append(student)


def save_file():
    


def main():
    print("Welcome to Student Database.\n\n")
    flag = True

    while flag:
        student_name = input("Enter Student name:\n\t")
        student_id = input("Enter Student Id :\n\t")
        add_student(student_name,student_id)
        more_students = input("Do you want to add another Student detail ? or Exit(Q)\n")
        if more_students=="Q":
            flag=False

    print_students_titlecase()

    print_student_details()


main()
#print(students)
