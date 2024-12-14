import string

alphabet = string.ascii_lowercase
alph_c = "badcfehgjilknmporqtsvuxwzy"

def crypt(text):
    
    rez = ""
    for c in text:
        if c != " ":
            i = alphabet.find(c)
            rez=rez+alph_c[i]
        else:
             rez=rez+" "
    return rez
     
def decrypt(text):
    
    rez = ""
    for c in text:
        if c != " ":
            i = alph_c.find(c)
            
            rez=rez+alphabet[i]
        else:
             rez=rez+" "
    return rez

in_str = input("Введите текст - ")
out_str = crypt(in_str)
print(out_str)
print(decrypt(out_str))