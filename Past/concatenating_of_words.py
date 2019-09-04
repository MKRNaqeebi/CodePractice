# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import itertools


def consective_char_count(word):
    count = 0
    max = 0
    current_char = ''
    for char in word:
        if char == current_char:
            count += 1
        else:
            current_char = char
            if count > max:
                max = count
            count = 1

    if count > max:
        max = count
    return max


def solution(words):
    # write your code in Python 3.6
    final_array = list(itertools.permutations(words))
    my_max = 0

    for word in final_array:
        if my_max < consective_char_count(''.join(word)):
            my_max = consective_char_count(''.join(word))

    return my_max


print(solution(["aabb", "aaaa", "bbab"]))
print(solution(["abcd", "aadxddd", 'dxxxxxdd']))
print(solution(['xxbxx', 'xbx', 'x'])==4)
print(solution(['dd', 'bb', 'cc', 'dd'])==4)
