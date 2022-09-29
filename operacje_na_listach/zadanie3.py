def reject(lista):
    parzyste=[]
    for i in lista:
        if i%2==0:
            parzyste.append(i)
    return parzyste
print(reject([1,2,3,4,5,6,7,8,]))