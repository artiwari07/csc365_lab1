
#Function to read students.txt and make it a list of dictionaries
def read_file(student_file):
    students_info = []
    with open(student_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 8:
                student = {
                    "last_name": parts[0].strip(),
                    "first_name": parts[1].strip(),
                    "grade": int(parts[2].strip()),
                    "classroom": int(parts[3].strip()),
                    "bus": int(parts[4].strip()),
                    "gpa": float(parts[5].strip()),
                    "teacher_last": parts[6].strip(),
                    "teacher_first": parts[7].strip()
                }
                students_info.append(student)

    return students_info

#Function to find students by last name S: <last name>
def SearchStudent_LastName(students_info, last_name):
    found = False
    for student in students_info:
        if student["last_name"] == last_name:
            print(f'{student["last_name"]}, {student["first_name"]}, Grade: {student["grade"]}, '
                  f'Classroom: {student["classroom"]}, Teacher: {student["teacher_last"]}, {student["teacher_first"]}')
            found = True

    if not found:
        print(f"No students found with last name: {last_name}")

#Function to find students by last name and give bus S: <last name> B
def SearchLastName_BusRoute(students_info, last_name):
    found = False
    for student in students_info:
        if student["last_name"] == last_name:
            print(f'{student["last_name"]}, {student["first_name"]}, Bus: {student["bus"]}')
            found = True
        
    if not found:
        print(f"No students found with last name: {last_name}")

#Function to find students with teacher's last name T: <last name>
def SearchStudent_TeacherLastName(students_info, last_name):
    found = False
    for student in students_info:
        if student["teacher_last"] == last_name:
            print(f'{student["last_name"]}, {student["first_name"]}')
            found = True
    
    if not found:
        print(f"No students found with teachers with last name: {last_name}")

#Function to find students with grade G: number
def SearchStudent_WithGrade(students_info, grade):
    found = False
    for student in students_info:
        if student["grade"] == grade:
            print(f'{student["last_name"]}, {student["first_name"]}')
            found = True
    
    if not found:
        print(f"No students found with grade: {grade}")

#TODO: Function to find students by bus route B: number
# def SearchStudent_WithBus(students_info, bus):

#TODO: Function to find students with higher gpa G: number H
# def SearchStudent_HigherGPA(students_info, grade):

#TODO: Function to find students with higher gpa G: number L
# def SearchStudent_LowerGPA(students_info, grade):

#TODO: Funtion to find average of gpa of students with the same grade A: number
# def Average_GPA(students_info, grade):

#TODO: Function to print info of students in ascending order by grade I
# def Print_StudentInfo(student_info):

def main():
    student_info = read_file('students.txt')
    # print(student_info)
    if not student_info:
        return
    
    while True:
        command = input("\nEnter a command (S[tudent], T[eacher], B[us], G[rade], A[verage], I[nfo], Q[uit]): ")
        if command.startswith('S:'):
            _, last_name = command.split(':')
            if 'B' in last_name:
                last_name = last_name.replace('B', '').strip()
                SearchLastName_BusRoute(student_info, last_name)
            else:
                SearchStudent_LastName(student_info, last_name.strip())
        elif command.startswith('T:'):
            _, last_name = command.split(':')
            SearchStudent_TeacherLastName(student_info, last_name.strip())
        elif command.startswith('G:'):
            _, grade_data = command.split(':')
            if 'H' in grade_data:
                grade = int(grade_data.replace('H', '').strip())
                SearchStudent_HigherGPA(student_info, grade)
            elif 'L' in grade_data:
                grade = int(grade_data.replace('L', '').strip())
                SearchStudent_LowerGPA(student_info, grade)
            else:
                SearchStudent_WithGrade(student_info, int(grade_data.strip()))
        # elif command.startswith('B:'):
        #     _, bus_route = command.split(':')
        #     SearchStudent_WithBus(student_info, int(bus_route.strip()))
        # elif command.startswith('A:'):
        #     _, grade = command.split(':')
        #     Average_GPA(student_info, int(grade.strip()))
        # elif command == 'I':
        #     Print_StudentInfo(student_info)
        elif command == 'Q':
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
