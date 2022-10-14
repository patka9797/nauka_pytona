import string


def remove_n(str, n):
    
    first= str[:n]
    last= str[n+1:]
    return first + last

print(remove_n('szklanka', 1))
