def change_sign(string,n):
    str1= string[0:n].lower()
    
    str2=string[n:]
    new_str= str1 + str2
    return new_str
print(change_sign('KOCICA',2))  