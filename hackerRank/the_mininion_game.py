# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .

# Constraints
# Lenght of string will be less than 10 to the power 6

def minion_game(string):
    # your code goes here
    stuart=0
    kevin=0
    for i in range(len(string)):
        if string[i] in "AEIOUaeiou":
            kevin+=len(string)-i
            print(kevin)
        else:
            stuart+=len(string)-i
            print(stuart)
    # if kevin>stuart:
    #     print("Kevin",kevin)        
    # elif stuart>kevin:
    #     print("Stuart",stuart)
    # else:
    #     print("Draw")
    # vowels = [ 'A','E','I','O','U',]
    # constant_words = 0
    # vowel_words = 0
    
    # for value in range(0,len(string)+1,1):
    #     for letter in range(0,len(string)+1,1):
    #         substring = string[0:letter]
    #         # print(substring)
    #         if len(substring) > 0:

                
    #             if substring[0] in vowels:
    #                 vowel_words = vowel_words + 1
    #             else:
    #                 constant_words = constant_words + 1
    #     string = string[1:]

    # if vowel_words > constant_words:
    #     print(f'Kevin {vowel_words}')
    # elif vowel_words < constant_words:
    #     print(f'Stuart {constant_words}')
    # else:
    #     print('Draw')
    

if __name__ == '__main__':
    s = input()
    minion_game(s)