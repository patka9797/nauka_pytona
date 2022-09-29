def power(lista):
    kwadrat=[]
    for i in lista:
        kwadrat.append(i**2)#potęgowanie liczb
    return kwadrat
print(power([2,4,6,8]))

def power2(lista, wykładnik):
    dowolne=[]
    for i in lista:
        dowolne.append(i**wykładnik)
    return dowolne
print(power2([3,4,5,6,6], 3))