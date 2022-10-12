def change_sign(string, sign,from_to):
    change_string=' '
    for i in string:
        if i==sign:
            change_string += from_to
        else:
            change_string += i
    return change_string
print(change_sign('kuń','u', 'o'))

