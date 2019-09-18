"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""


def solution(A):
    best_start, best_end = -1, 0
    max_sum = 0
    temp_sum = 0
    temp_start = -1
    for idx, val in enumerate(A):
        temp_sum = temp_sum + val
        if max_sum < temp_sum:
            best_end = idx
            max_sum = temp_sum
            best_start = temp_start
            continue
        if temp_sum < 0:
            temp_start = idx
            temp_sum = 0
    if best_end - best_start > 1:
        result = sum(A[best_start+1: best_end+1])
        if result:
            return result
    return max(A)


# print(solution([34, -50, 42, 14, -5, 86]))
# print(solution([-5, -1, -8, -9]))
# print(solution([-2, -5, 6, -2, -3, 1, 5, -6]))
# print(solution([3,2,-3,-1,1,-3,1,-1]))
print(solution([-2,-1]))
