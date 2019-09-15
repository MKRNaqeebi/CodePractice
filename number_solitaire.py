# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def find_min(I, A):
    min_item = max(A[I-5:I+1])
    max_index = I
    J = I - 5
    while J <= max_index:
        if A[J] == min_item:
            I = J
        J = J + 1
    return I

def solution(A):
    # write your code in Python 3.6
    best_sum = 0
    count = 0
    I = 1
    while True:
        if I > len(A)-2:
            break

        if A[I] > 0:
            best_sum = best_sum + A[I]
            count = 0
        else:
            count += 1
        if count == 6:
            # best_sum += A[I]
            count = 0
            I = find_min(I, A)
            best_sum += A[I]
        I = I + 1

    return best_sum + A[0] + A[-1]

solution([0,2,-5,-1,-5,-6,-5,-6,-6])
