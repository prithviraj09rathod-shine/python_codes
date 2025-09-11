#convert from upper to lower case
def convert_uppercaseTolowercase(s:str)->str:
    return s.swapcase()

def convert_lowercaseToupercase1(s:str)->str:
    if s.islower():
        s.upper()
    else:
        s.lower()
    return s
print(convert_uppercaseTolowercase("Reshma"))
print(convert_lowercaseToupercase1("bAnAnA"))