def power(list_):
    square=[]
    for i in list_:
        square.append(i**2)#potęgowanie liczb
    return square
print(power([2, 4, 6, 8]))

def power2(list, exponent):
    any_=[]
    for i in list:
        any_.append(i**exponent)
    return any_
print(power2([3, 4, 5, 6, 6], 3))
