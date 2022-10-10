x = 1
y = 1 
z= 2
n = 3

i,j,k = 0,0,0

perms = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) != n]

print(perms)
