### adjust letter capitization

def myfunc(string): 
    return_string = ""
    for letter in string:
        if letter == letter.upper():
            return_string += letter.lower()
        elif letter == letter.lower():
            return_string += letter.upper()
    return (return_string)
myfunc('AnThOnY')