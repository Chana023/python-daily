# https://www.hackerrank.com/domains/algorithms?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=problem-solving

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    distance_to_nearest_station = 0
    list_of_minimum_distances = []

    for value in range(n):
        distance_to_nearest_station = 0
        prev_distance_to_nearest_station = n
        if value in c:
            distance_to_nearest_station  = 0
            list_of_minimum_distances.append(distance_to_nearest_station)
        else:
            for x in c:
                distance_to_nearest_station = abs(value - x)
                if distance_to_nearest_station <= prev_distance_to_nearest_station:
                    prev_distance_to_nearest_station = distance_to_nearest_station

            list_of_minimum_distances.append(prev_distance_to_nearest_station)

        

    print(max(list_of_minimum_distances))

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)


# Best solution:

# def flatlandSpaceStations(n, c):
# c.sort()
#   maxd = max(c[0], n-1 - c[-1])
#   for i in range(len(c)-1):
#     maxd = max((c[i+1]-c[i])//2, maxd)
#   return maxd
