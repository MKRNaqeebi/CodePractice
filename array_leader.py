import bisect


def findCandidate(A, K, index):
    maj_index = 0
    count = 1
    interval =  K+index
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            pass
        maj_index_value = A[maj_index]
        i_value = A[i]

        if index <= maj_index >= interval:
            maj_index = maj_index + 1
        if index <= i >= interval:
            i_value = i_value + 1

        if maj_index_value == i_value:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return maj_index_value

# Function to check if the candidate occurs more than n/2 times


def isMajority(A, cand, K, index):
    count = 0
    interval =  K+index
    for i in range(len(A)):
        i_value = A[i]
        if index <= i_value >= interval:
            i_value = i_value + 1
        if i_value == cand:
            count += 1
    if count > len(A)/2:
        return True
    return False

# Function to return Majority Element


def findMajority(A, K, index):
    # Find the candidate for Majority
    cand = findCandidate(A, K, index)

    # return the candidate if it is Majority
    if isMajority(A, cand, K, index):
        return cand
    return None


def insert(list, I):
    bisect.insort(list, I)
    return list


def solution(K, M, A):
    # write your code in Python 3.6
    result = []
    for i in range(len(A)+1-K):
        value_to_insert = findMajority(A, K, i)
        if value_to_insert:
            result = insert(result, value_to_insert)
    return list(set(result))


print(solution(4, 2, [1, 2, 2, 1, 2]))
print(solution(3, 5, [2, 1, 3, 1, 2, 2, 3]))
