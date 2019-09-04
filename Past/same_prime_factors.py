import math 

def primeFactors(first, second):
    n = first
    if first < second:
        n = second

    if first % 2 == 0 and second % 2 > 0:
        return False
    if second % 2 == 0 and first % 2 > 0:
        return False
    while first % 2 == 0:
        first = first / 2
    while second % 2 == 0:
        second = second / 2
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2): 

        if first % i == 0 and second % i > 0:
            return False
        if second % i == 0 and first % i > 0:
            return False

        while first % i == 0:
            first = first / i
        while second % i == 0:
            second = second / i
              
    # Condition if n is a prime 
    # number greater than 2 
    if first > 2 and second % first > 0:
        return False
        
    if second > 2 and first % second > 0:
        return False
    return True

def solution(A, B):
    count = 0
    for a_item, b_item in zip(A,B):
        if primeFactors(a_item, b_item):
            count += 1
    return count


print(solution([15, 10, 9], [75, 30, 5]))
