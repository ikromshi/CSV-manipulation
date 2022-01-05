def calc_avg_for_assn(grade_table, column_index):
    '''
    :return: the average grade across all students for the assignment in the given column of the grade_table,
            or -1 if the column index is invalid
    '''

    if len(grade_table[0]) <= column_index:
        return -1

    if column_index < 0:
        return -1

    total = 0
    for r in range(len(grade_table)):
        total = total + grade_table[r][column_index]

    return total / len(grade_table)


def calc_avg_for_student(grade_table, row_index):
    '''
    :return: the average grade across all assignments for the student in the given row of the grade_table,
            or -1 if the row index number is invalid
    '''

    if row_index >= len(grade_table):
        return -1

    if row_index < 0:
        return -1

    total = 0
    for i in range(len(grade_table[row_index])):
        total += grade_table[row_index][i]

    return total/len(grade_table[row_index])


def find_min_grade_on_assn(grade_table, column_index):
    '''
    :return: the lowest grade on the assignment in the given column of the grade_table,
           or -1 if the column number is invalid
    '''

    if len(grade_table[0]) <= column_index:
        return -1

    if column_index < 0:
        return -1

    total = []
    for i in range(len(grade_table)):
        total.append(grade_table[i][column_index])

    return min(total)


def find_min_grade_for_student(grade_table, row_index):
    '''
    :return: the lowest grade for the student in the given row of the grade_table,
           or -1 if the row index is invalid
    '''

    if row_index >= len(grade_table):
        return -1

    if row_index < 0:
        return -1

    total = []
    for i in range(len(grade_table[row_index])):
        total.append(grade_table[row_index][i])

    return min(total)


def add_student_record(student_list, grade_table, student_record_str):
    """
    :param student_list: a list of all student names, to add a new student to
    :param grade_table: a 2D list of all student grades, to add a new list of grades to
    :param student_record_str: the string containing the student's name and all the grades, comma separated
    :Side effects:  the new name is added to the end of student_list, and the grades are added as a row to the end of
    the grade_table
    """
    record_list = list(student_record_str)
    while "\n" in record_list:
        record_list.remove("\n")
    new_str = ""

    for val in record_list:
        new_str += val
    new_str = new_str.split(",")
    student_list.append(new_str[0])

    grades = []
    for i in range(1, len(new_str)):
        grades.append(int(new_str[i]))
    grade_table.append(grades)


def read_file(filename):
    my_file = open(filename, "r")
    all_lines = my_file.readlines()
    my_file.close()
    return all_lines


def main():
    # TODO:LEVEL2

    print("LEVEL 2")
    fn = "gradeData1.csv"
    student_records = read_file(fn)

    student_list = []
    grade_list = []
    for data in student_records:
        add_student_record(student_list, grade_list, data)
    print("STUDENT LIST:", student_list)
    print("GRADE LIST:", grade_list)

    # TODO: LEVEL3
    print("\nLEVEL 3")
    file = input("Enter the name of the spreadsheet: ")
    print(f"Summary for {file}:")
    student_records = read_file(file)

    student_list = []
    grade_list = []
    for data in student_records:
        add_student_record(student_list, grade_list, data)

    # DATA FOR STUDENT
    print("\nStudent\t Lowest\t Average")
    print("------------------------")
    for i in range(len(student_list)):
        min_val = find_min_grade_for_student(grade_list, i)
        avg = calc_avg_for_student(grade_list, i)
        print(f"{student_list[i]}\t {min_val}\t\t {avg}")

    # DATA FOR ASSIGNMENT
    print("\nAssgn\t Lowest\t Average")
    print("------------------------")
    for i in range(len(grade_list[0])):
        min_val = find_min_grade_on_assn(grade_list, i)
        avg = calc_avg_for_assn(grade_list, i)
        print(f"{i}\t {min_val}\t\t {avg}")


if __name__ == "__main__":
    main()
