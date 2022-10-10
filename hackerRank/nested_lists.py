if __name__ == '__main__':
    mini_list = []
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        mini_list = [name,score]
        nested_list.append(mini_list)

    score_list = []

    for position in range(len(nested_list)):
        score_list.append(nested_list[position][1])

    score_list.sort(reverse=False)

    for value in score_list:
        if value != score_list[0]:
            second_lowest = value
            break

    print(second_lowest)  

    students_with_lowest_grades = []

    for item in range(len(nested_list)):
        if nested_list[item][1] == second_lowest:
            students_with_lowest_grades.append(nested_list[item][0])

    students_with_lowest_grades.sort()

for student in students_with_lowest_grades:
    print(student)