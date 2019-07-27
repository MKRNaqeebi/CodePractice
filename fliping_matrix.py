# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def is_opposite(A, B):
    for i in range(len(A)):
        if A[i]==B[i]:
            return False
    return True

def solution(A):
    # write your code in Python 3.6
    max_rows = 0
    rows = len(A)
    cols = len(A[0])
    for row in range(rows):
        count = 0
        for i in range(rows-row):
            if A[row]==A[i+row] or is_opposite(A[row], A[i+row]):
                count+=1
        if count>max_rows:
            max_rows = count
    return max_rows


print(solution([[0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 1]]))
print(solution([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]))
