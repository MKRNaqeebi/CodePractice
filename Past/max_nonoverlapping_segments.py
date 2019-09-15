# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    I = 0
    P = -1
    result = []
    N = len(A)
    if N<=1: return N
    while True:
        if(I>=N):
            break

        if A[I] <= P:
            I = I + 1
            continue

        if I+1 >= N:
            result.append(I)
            break

        if (A[I] <= A[I+1] and A[I+1] <= B[I]) or (A[I+1] <= A[I] and A[I] <= B[I+1]):
            if B[I+1] >= B[I]:
                result.append(I)
                P = B[I]
            else:
                result.append(I+1)
                P = B[I+1]
            I = I + 2
        else:
            result.append(I)
            P = B[I]
            I = I + 1

    return len(result)


print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]))
print(solution([], []))
print(solution([1, 3, 5, 7, 9,], [2]))
