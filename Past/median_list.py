# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import statistics

def solution(given_list):
    middle_list = []
    results = []
    for item in given_list:
        middle_list.append(item)
        results.append(statistics.median(middle_list))
    return results

print(solution([2, 1, 5, 7, 2, 0, 5]))
