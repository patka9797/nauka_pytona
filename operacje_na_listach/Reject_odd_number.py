def reject_odd_numer(list):
    even=[]
    for i in list:
        if i%2== 0:# jeśli reszta z dzielenia =0, liczby parzyste
            even.append(i)
    return even
print(reject_odd_number([1, 2, 3, 4, 5, 6, 7, 8]))
