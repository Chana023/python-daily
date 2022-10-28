width = int(input())
letter = 'H'
space = ' '

# Top arrow
for x in range(width):
     print(((letter * ((2*x)+1)).rjust(width+x,space)) + space.ljust(width-x-1,space)) 

for y in range(width+1):
    print((letter*width).center(width*2,space) + space.center(width*2,space) + (letter*width).center(width*2,space))

for z in range(width - 2):
     print((letter*width*5).center(width*6,space))

for y in range(width+1):
    print((letter*width).center(width*2,space) + space.center(width*2,space) + (letter*width).center(width*2,space))

for x in range(width):
     print(((letter*(width-x-1)).rjust(width)+letter+(letter*(width-x-1)).ljust(width)).rjust(width*6))