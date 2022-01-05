from main import calc_avg_for_assn, calc_avg_for_student, find_min_grade_on_assn, find_min_grade_for_student, add_student_record


def calc_avg_for_assn_test():
    print("----------calc_avg_for_assn_test------------")
    test_grade_table = [[10, 9, 10],
                        [8, 6, 8],
                        [3, 5, 9],
                        [0, 0, 0]]

    print("Should be 5.25:\t", calc_avg_for_assn(test_grade_table, 0))
    print("Should be 5.0:\t", calc_avg_for_assn(test_grade_table, 1))
    print("Should be 6.75:\t", calc_avg_for_assn(test_grade_table, 2))
    print("Should be -1:\t", calc_avg_for_assn(test_grade_table, 3))
    print("Should be -1:\t", calc_avg_for_assn(test_grade_table, -1))


def calc_avg_for_student_test():
    print("----------calc_avg_for_student_test------------")
    test_grade_table = [[10, 9, 10],
                        [8, 6,  8],
                        [3, 5,  9],
                        [0, 0,  0]]
    print("Should be 9.666...:\t", calc_avg_for_student(test_grade_table, 0))
    print("Should be 7.333...:\t", calc_avg_for_student(test_grade_table, 1))
    print("Should be 5.666...:\t", calc_avg_for_student(test_grade_table, 2))
    print("Should be 0.0:\t", calc_avg_for_student(test_grade_table, 3))
    print("Should be -1:\t", calc_avg_for_student(test_grade_table, 4))
    print("Should be -1:\t", calc_avg_for_student(test_grade_table, -1))


def find_min_grade_on_assn_test():
    print("----------find_min_grade_on_assn_test------------")
    test_grade_table = [[10, 9, 10],
                        [8, 6,  8],
                        [3, 5,  9],
                        [0, 0,  1]]
    print("Should be 0:\t", find_min_grade_on_assn(test_grade_table, 0))
    print("Should be 0:\t", find_min_grade_on_assn(test_grade_table, 1))
    print("Should be 1:\t", find_min_grade_on_assn(test_grade_table, 2))
    print("Should be -1:\t", find_min_grade_on_assn(test_grade_table, 3))
    print("Should be -1:\t", find_min_grade_on_assn(test_grade_table, -1))


def find_min_grade_for_student_test():
    print("----------find_min_grade_for_student_test------------")
    test_grade_table = [[10, 9, 10],
                        [8, 6, 8],
                        [3, 5, 9],
                        [0, 0, 0]]
    print("Should be 9:\t", find_min_grade_for_student(test_grade_table, 0))
    print("Should be 6:\t", find_min_grade_for_student(test_grade_table, 1))
    print("Should be 3:\t", find_min_grade_for_student(test_grade_table, 2))
    print("Should be 0:\t", find_min_grade_for_student(test_grade_table, 3))
    print("Should be -1:\t", find_min_grade_for_student(test_grade_table, 4))
    print("Should be -1:\t", find_min_grade_for_student(test_grade_table, -1))


def add_student_record_test():
    print("----------add_student_record_test------------")
    # start with some data
    test_student_list = ["Shelly"]
    test_grade_table = [[10, 9, 10]]
    # add some more
    add_student_record(test_student_list, test_grade_table, "Maria,8,6,8\n")  # when read from file, sometimes has \n
    add_student_record(test_student_list, test_grade_table, "Ed,3,5,9\n")
    add_student_record(test_student_list, test_grade_table, "Susan,0,0,0")  # other times no \n
    # Test for certain values
    print("Should be [3,5,9]:\t", test_grade_table[2])
    print("Should be Susan:\t", test_student_list[3])
    # Test to make sure things in table are numbers
    print("Should be True:\t", test_grade_table[1][1] == 6)
    print(test_grade_table)


def main():
    # calc_avg_for_assn_test()
    # calc_avg_for_student_test()
    # find_min_grade_on_assn_test()
    # find_min_grade_for_student_test()
    # TODO: uncomment below when ready to test add_student_record
    add_student_record_test()


main()
