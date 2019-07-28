# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def get_opposite(A):
    result = ''
    for item in A:
        if item=='0':
            result+='1'
        else:
            result+='0'
    return result

def solution(A):
    # write your code in Python 3.6
    max_rows = 0
    rows = len(A)
    hash_table = {} 
    for row in A:
        row_str = ''.join(str(e) for e in row)
        # print(row_str, get_opposite(row_str))
        if row_str in hash_table:
            hash_table[row_str] += 1
        elif get_opposite(row_str) in hash_table:
            hash_table[get_opposite(row_str)] += 1
        else: 
            hash_table[row_str] = 1
    for key in hash_table: 
        if hash_table[key] > max_rows: 
            max_rows = hash_table[key]
    return max_rows


print(solution([[0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 1, 1]]))
print(solution([[0, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]))
