#Write a function named capital_indexes. The function takes a single parameter, which is a string. 
#Your function should return a list of all the indexes in the string that have capital letters.

#For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

from curses.ascii import isupper


def capital_indexes(word):

    capital_indexes = []
    index = 0
    for letter in word:
        if letter.isupper():
            capital_indexes.append(index)
        index += 1

    print(capital_indexes)
            

capital_indexes('HeLlO')
