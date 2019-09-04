# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, F):
    # write your code in Python 3.6
    N = len(A)
    G = N - F
    result = 0
    C = [0] * N
    range_n = range(N)
    
    for index in range_n:
        if A[index] > B[index]:
            C[index] = A[index] - B[index]
    D = [0] * N
    
    for index in range_n:
        if A[index] < B[index]:
            D[index] = B[index] - A[index]

    for index in range_n:

        a_index_max, a_max_value = max(enumerate(C), key=lambda p: p[1])
        b_index_max, b_max_value = max(enumerate(D), key=lambda p: p[1])

        if C[a_index_max] > D[b_index_max] and F > 0 or G == 0:
            result += A[a_index_max]
            F -= 1
            C[a_index_max] = -1
            D[a_index_max] = -1
            continue
        result += B[b_index_max]
        G -= 1
        D[b_index_max] = -1
        C[b_index_max] = -1
    return result

print(solution([4, 2, 1], [2, 5, 3], 2) ==10)
print(solution([14, 2, 14, 31, 30], [4, 1, 4, 30, 31], 2) )
print(solution([4, 1, 4, 30, 31], [14, 2, 14, 31, 30], 2) )
print(solution([5, 5, 5], [5, 5, 5], 1)  ==15)
print(solution([5,10,20,30],[30,100,15,20], 3)==155)
