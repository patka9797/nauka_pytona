def replace_(str1):
    maketrans= str1.maketrans
    final=str1.translate(maketrans(',.', '.,', ' '))
    return final 
print(replace_('213,345.2'))