def add_ing(string):
    
    if string.endswith('ing'):
        string += 'ly'
    
    elif len(string)>=3:
        string += 'ing'
    else:
        return string
    return string 
print(add_ing('osaing'))



