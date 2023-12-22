# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers

    n = int(n)
    if n == 0:
        fib_list = []
        return fib_list
    if n == 1:
        fib_list = [0]
        return fib_list

    fib_list = [0,1]

    for value in range(n-1):
        
        if value >= 1:
            result = fib_list[value] + fib_list[value-1]
            fib_list.append(result)
    
    return fib_list
        
        

if __name__ == '__main__':

    n = input()
    print(list(map(cube,fibonacci(n))))