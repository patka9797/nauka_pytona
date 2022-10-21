import string


def remove_n_first_characters(str, n):
    
    first= str[:n]
    last= str[n+1:]
    return first + last

print(remove_n_first_characters('szklanka', 1))
