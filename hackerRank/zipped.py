# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

N, X = input().split(' ')

student_list = [0,0,0,0,0]
subjects_list = []

for subject in range(int(X)):
    
    subjects_list.append(list(map(float,input().split())))

for tup in zip(*subjects_list):
    print(sum(tup)/int(X))
