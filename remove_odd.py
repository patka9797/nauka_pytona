def remove_odd(string):
    string2=' '
    for i in range(1, len(string)+1):
        if i%2== 0:
            string2 +=  string[i-1]
    return string2
print(remove_odd('abcdefg'))
