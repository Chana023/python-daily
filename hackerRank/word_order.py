# https://www.hackerrank.com/challenges/word-order/problem

number_words = int(input())

word_dict = {}

for value in range(number_words) :
    word = input()

    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(len(word_dict))
answer = ' '.join(f'{value}' for key, value in word_dict.items())

print(answer)




