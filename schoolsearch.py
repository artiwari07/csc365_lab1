# Function to read students list from list.txt and make it a list of dictionaries
def read_list(student_file):
    students_info = []
    with open(student_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 6:
                student = {
                    "last_name": parts[0].strip(),
                    "first_name": parts[1].strip(),
                    "grade": int(parts[2].strip()),
                    "classroom": int(parts[3].strip()),
                    "bus": int(parts[4].strip()),
                    "gpa": float(parts[5].strip())
                }
                students_info.append(student)
    return students_info

# Function to read teachers info from teachers.txt
def read_teachers(teacher_file):
    teachers_info = []
    with open(teacher_file, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                teacher = {
                    "last_name": parts[0].strip(),
                    "first_name": parts[1].strip(),
                    "classroom": int(parts[2].strip()),
                }
                teachers_info.append(teacher)
    return teachers_info

# Function to find students by last name S: <last name>
def SearchStudent_LastName(students_info, teachers_info, last_name):
    found = False
    for student in students_info:
        if student["last_name"] == last_name:
            print(f'{student["last_name"]}, {student["first_name"]}, Grade: {student["grade"]}, '
                  f'Classroom: {student["classroom"]}')
            for teacher in teachers_info:
                if teacher["classroom"] == student["classroom"]:
                    print(f'Teacher: {teacher["last_name"]}, {teacher["first_name"]}')
            print(f'')
            found = True
    if not found:
        print(f"No students found with last name: {last_name}")

# Function to find students by last name and give bus S: <last name> B
def SearchLastName_BusRoute(students_info, last_name):
    found = False
    for student in students_info:
        if student["last_name"].lower() == last_name.lower():
            print(f'{student["last_name"]}, {student["first_name"]}, Bus: {student["bus"]}')
            found = True
    if not found:
        print(f"No students found with last name: {last_name}")

# Function to find students with teacher's last name T: <last name>
def SearchStudent_TeacherLastName(teachers_info, students_info, last_name):
    found = False
    for teacher in teachers_info:
        if teacher["last_name"] == last_name:
            for student in students_info:
                if student["classroom"] == teacher["classroom"]:
                    print(f'{student["last_name"]}, {student["first_name"]}')
                    found = True
    if not found:
        print(f"No students found with teachers with last name: {last_name}")

# Function to find students with grade G: number
def SearchStudent_WithGrade(students_info, grade):
    found = False
    for student in students_info:
        if student["grade"] == grade:
            print(f'{student["last_name"]}, {student["first_name"]}')
            found = True
    if not found:
        print(f"No students found with grade: {grade}")

# Function to find students by bus route B: number
def SearchStudent_WithBus(students_info, bus):
    found = False
    for student in students_info:
        if student["bus"] == bus:
            print(f'{student["last_name"]}, {student["first_name"]}, Grade: {student["grade"]}, Classroom: {student["classroom"]}')
            found = True
    if not found:
        print(f"No students found with bus route: {bus}")

#PRINT OUT TEACHER AS WELL
# Function to find students with highest GPA G: number H
def SearchStudent_HigherGPA(students_info, teachers_info, grade):
    students_in_grade = [student for student in students_info if student["grade"] == grade]
    if students_in_grade:
        highest_gpa_student = max(students_in_grade, key=lambda x: x["gpa"])
        print(f'{highest_gpa_student["last_name"]}, {highest_gpa_student["first_name"]}, '
              f'GPA: {highest_gpa_student["gpa"]}, Bus: {highest_gpa_student["bus"]}')
    else:
        print(f"No students found in grade {grade}")

#PRINT OUT TEACHER AS WELL
# Function to find students with lowest GPA G: number L
def SearchStudent_LowerGPA(students_info, teachers_info, grade):
    students_in_grade = [student for student in students_info if student["grade"] == grade]
    if students_in_grade:
        lowest_gpa_student = min(students_in_grade, key=lambda x: x["gpa"])
        print(f'{lowest_gpa_student["last_name"]}, {lowest_gpa_student["first_name"]}, '
              f'GPA: {lowest_gpa_student["gpa"]}, Bus: {lowest_gpa_student["bus"]}')
    else:
        print(f"No students found in grade {grade}")

# Function to calculate average GPA of students in a grade A: number
def Average_GPA(students_info, grade):
    students_in_grade = [student for student in students_info if student["grade"] == grade]
    if students_in_grade:
        avg_gpa = sum(student["gpa"] for student in students_in_grade) / len(students_in_grade)
        print(f'Grade {grade}, Average GPA: {avg_gpa:.2f}')
    else:
        print(f"No students found in grade {grade}")

# Function to print number of students in each grade I
def Print_StudentInfo(students_info):
    grade_counts = {}
    for student in students_info:
        grade = student["grade"]
        if grade not in grade_counts:
            grade_counts[grade] = 0
        grade_counts[grade] += 1
    for grade in sorted(grade_counts):
        print(f'Grade {grade}: {grade_counts[grade]} students')

# Function to find all students in a specific classroom SC: <number>
def SearchStudents_InClassroom(students_info, classroom):
    found = False
    for student in students_info:
        if student["classroom"] == classroom:
            print(f'{student["last_name"]}, {student["first_name"]}')
            found = True
    if not found:
        print(f"No students found in classroom: {classroom}")

# Function to find teachers in a specific classroom TC: <number>
def SearchTeachers_InClassroom(teachers_info, classroom):
    found = False
    for teacher in teachers_info:
        if teacher["classroom"] == classroom:
            print(f'{teacher["last_name"]}, {teacher["first_name"]}')
            found = True
    if not found:
        print(f"No teachers found in classroom: {classroom}")

# Function to find all teachers for a specific grade TG: <number>
def SearchTeachers_InGrade(teachers_info, students_info, grade):
    found = False
    printed_teachers = set()  # Set to track printed teacher names
    for student in students_info:
        if student["grade"] == grade:
            for teacher in teachers_info:
                if student["classroom"] == teacher["classroom"]:
                    teacher_name = f'{teacher["last_name"]}, {teacher["first_name"]}'
                    if teacher_name not in printed_teachers:
                        print(teacher_name)
                        printed_teachers.add(teacher_name)  # Add to the set
                        found = True
    if not found:
        print(f"No teachers found teaching grade: {grade}")

def main():
    students_info = read_list('list.txt')
    teachers_info = read_teachers('teachers.txt')
    
    while True:
        command = input("\nEnter a command (S[tudent], T[eacher], B[us], G[rade], A[verage], I[nfo], SC: <number>, TC: <number>, TG: <number>, Q[uit]): ")
        if command.startswith('S:'):
            _, last_name = command.split(':')
            if 'B' in last_name:
                last_name = last_name.replace('B', '').strip()
                SearchLastName_BusRoute(students_info, last_name)
            else:
                SearchStudent_LastName(students_info, teachers_info, last_name.strip())
        elif command.startswith('T:'):
            _, last_name = command.split(':')
            SearchStudent_TeacherLastName(teachers_info, students_info, last_name.strip())
        elif command.startswith('G:'):
            _, grade_data = command.split(':')
            if 'H' in grade_data:
                grade = int(grade_data.replace('H', '').strip())
                SearchStudent_HigherGPA(students_info, teachers_info, grade)
            elif 'L' in grade_data:
                grade = int(grade_data.replace('L', '').strip())
                SearchStudent_LowerGPA(students_info, teachers_info, grade)
            else:
                grade = int(grade_data.strip())
                SearchStudent_WithGrade(students_info, grade)
        elif command.startswith('B:'):
            _, bus = command.split(':')
            SearchStudent_WithBus(students_info, int(bus.strip()))
        elif command.startswith('A:'):
            _, grade = command.split(':')
            Average_GPA(students_info, int(grade.strip()))
        elif command.startswith('I'):
            Print_StudentInfo(students_info)
        elif command.startswith('SC:'):
            _, classroom = command.split(':')
            SearchStudents_InClassroom(students_info, int(classroom.strip()))
        elif command.startswith('TC:'):
            _, classroom = command.split(':')
            SearchTeachers_InClassroom(teachers_info, int(classroom.strip()))
        elif command.startswith('TG:'):
            _, grade = command.split(':')
            SearchTeachers_InGrade(teachers_info, students_info, int(grade.strip()))
        elif command == 'Q':
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
