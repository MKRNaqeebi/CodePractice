
def solution(A):
    best_start, best_end = 0, 0
    max_sum = 0
    temp_sum = 0
    for idx, val in enumerate(A):
        
        temp_sum = temp_sum + val

        if max_sum < temp_sum:
            best_end = idx
            max_sum = temp_sum
            continue
        if temp_sum < 0:
            best_start = idx
            best_end = idx
            max_sum = 0
            temp_sum = 0

    return sum(A[best_start+1: best_end+1])

print(solution([34, -50, 42, 14, -5, 86]))
print(solution([-5, -1, -8, -9]))
print(solution([-2, -5, 6, -2, -3, 1, 5, -6]))
