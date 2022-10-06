def take(list_, number_of_items):
    empty=[]
    for i in list_:
        if len(empty)== number_of_items:
            return emppty
        else:
            empty.append(i)
    return empty# return poza pętlą for dlatego, że jeśli lista jest mniejsza niż założona l. elementów i tak zwraca
print(take([1, 2, 4, 6, 7, 8], 50))
