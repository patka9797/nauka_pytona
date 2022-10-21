from pkg_resources import to_filename


def first_sign(string,sign,from_to):
    change_first_sign=' '
    was_change=False
    for i in string:
        if i==sign and not was_change:
            change_first_sign += from_to
            was_change=True
        else: 
            change_first_sign += i
    return change_first_sign
print(first_sign('koon', 'o', 'e'))