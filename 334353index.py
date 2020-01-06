
def getChange(a, b):
    coin_list = [1, 0.5, 0.25,  0.1, 0.05, 0.01]
    results = [0, 0, 0, 0,  0, 0]
    return_change = a - b
    for index in range(6):
        if return_change:
            while True:
                if return_change < coin_list[index]:
                    break
                results[index] += 1
                return_change -= coin_list[index]
                return_change = round(return_change, 2)

    return results


print(getChange(5, 1.25))

print(getChange(3.14, 1.99)) # should return [0,1,1,0,0,1]
print(getChange(4, 3.14)) # should return [1,0,1,1,1,0]
print(getChange(0.45, 0.34)) # should return [1,0,1,0,0,0]

