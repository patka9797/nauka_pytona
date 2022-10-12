def concat(list_of_strings, separator):
    conected_string=''
    for i in list_of_strings:
        conected_string +=i + separator
    return conected_string
a=concat(['mleko','jajka','chleb'], ' ')
print(a)