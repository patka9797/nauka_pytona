def change(string, b,c):#zamienia pierwszy znam b na drugi znak c
    nowy=''
    for i in string:
        if i==b:
            nowy=nowy+c
        else:
            nowy=nowy+i#dodajemy do nowego po prostu i
    return nowy
print(change('+pasztet','+','-'))