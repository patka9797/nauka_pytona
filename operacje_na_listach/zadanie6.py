def take(lista,elementy):
    pusta=[]
    for i in lista:
        if len(pusta)==elementy:
            return pusta
        else:
            pusta.append(i)
    return pusta# return poza pętlą for dlatego, że jeśli lista jest mniejsza niż założona l. elementów i tak zwraca
print(take([1,2,4,6,7,8],50))
