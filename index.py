
def rpnCalculator(S):
    J=S
    result = 0
    my_list = []
    a, b = 0, 0

    if len(S.split(' '))==1:
        return int(J)

    for item in S.split(' '):
        if item == '':
            continue
        if item in ['+', "*"]:
            a = my_list.pop()
            b = my_list.pop()
            if item == '+':
                result = a+b
            elif item == '*':
                result = a*b
            my_list.append(result)
        else:
            my_list.append(int(item))

    return result


print(rpnCalculator("1 2 3 * + "))
print(rpnCalculator("2 1 + "))
print(rpnCalculator("1 2 + 3 * "))

print(rpnCalculator("1 2 3 * +"))
print(rpnCalculator("1156 12 11 * +") )#1288
print(rpnCalculator("5 2 + 3 *") ) #21
print(rpnCalculator("5 2 * 2 * 4 +"))# // 24
print(rpnCalculator("5 2 + 2 + 4 +"))# // 13
print(rpnCalculator("3 2 + 2 4 + *"))# // 30
print(rpnCalculator("3 2 2 4 + + *"))# // 24
print(rpnCalculator("5"))# // 5
print(rpnCalculator("0 1 *"))# // 0
print(rpnCalculator("5 5 + 6 6 + 1 1 + * +"))# // "10 12 2 * +" => 34
