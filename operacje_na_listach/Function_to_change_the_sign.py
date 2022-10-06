def change(string, b, c):#zamienia pierwszy znam b na drugi znak c
    new=''
    for i in string:
        if i== b:
            new += c
        else:
            new += i #dodajemy do nowego po prostu i
    return new
print(change('+pasztet', '+', '-'))
