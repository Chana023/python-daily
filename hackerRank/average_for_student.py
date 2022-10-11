if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    values_list = student_marks[query_name]
    average = 0
    for value in values_list:
        average  = average + value

    average = (average / 3)

    average = "{:.2f}".format(average)
    
    print(average)