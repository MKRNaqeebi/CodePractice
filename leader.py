
def findMajority(arr, size, start, end): 
    m = {} 
    for i in range(size): 
        i_value = arr[i]

        if i>=start and i<end:
            i_value +=1
        if i_value in m: 
            m[i_value] += 1
        else: 
            m[i_value] = 1
    for key in m: 
        if m[key] > size / 2: 
            return key
    return None

def solution(K, M, A):
    # write your code in Python 3.6
    result = []
    N = len(A)
    for i in range(len(A)+1-K):
        temp = findMajority(A, N, i, i+K)
        if temp:
            result.append(temp)
    return list(sorted(set(result)))


print(solution(3, 5, [2, 1, 3, 1, 2, 2, 3]) )
print(solution(4, 2, [1, 2, 2, 1, 2]))
