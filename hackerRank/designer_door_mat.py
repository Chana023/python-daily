N, M = map(int, input().split())

pattern = '.|.'
dash = '-'
dummy = 0

for x in range(N):
    if (x < (N/2)-1):
        print((pattern * ((2*x)+1)).center(M,dash) )
    elif(x == ((N-1)/2)):
        print('WELCOME'.center(M,dash) )
    elif(x > ((N-1)/2)):
        N_max = N -2
        print( (pattern *((-2*dummy) + N_max)).center(M,dash) )
        dummy = dummy + 1
    