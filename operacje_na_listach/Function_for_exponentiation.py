def power(list):
    square=[]
    for i in list:
        square.append(i**2)#potęgowanie liczb
    return square
print(power([2, 4, 6, 8]))

def power2(list, exponent):
    any=[]
    for i in list:
        any.append(i**exponent)
    return any
print(power2([3, 4, 5, 6, 6], 3))
