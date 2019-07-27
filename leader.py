import bisect  
import copy

def findMajority(arr, size): 
    m = {} 
    for i in range(size): 
        if arr[i] in m: 
            m[arr[i]] += 1
        else: 
            m[arr[i]] = 1
    count = 0
    for key in m: 
        if m[key] > size / 2: 
            count = 1
            return key
    if(count == 0): 
        return None

def find_leader_from_segment(K, A, N, index):
    temp = copy.deepcopy(A)
    for i in range(K):
        temp[index+i] = A[index+i]+1
    return findMajority(temp, N)

def insert(list, I): 
    bisect.insort(list, I)  
    return list

def solution(K, M, A):
    # write your code in Python 3.6
    result = []
    N = len(A)
    for i in range(len(A)+1-K):
        value_to_insert = find_leader_from_segment(K, A, N, i)
        if value_to_insert:
            if value_to_insert in result:
                pass
            else:
                result = insert(result,value_to_insert)
    return result
    


print(solution(3, 5, [2, 1, 3, 1, 2, 2, 3]) )

print(solution(4, 2, [1, 2, 2, 1, 2]))
