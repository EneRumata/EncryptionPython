import string

alphabet = string.ascii_lowercase
s = -500

def crypt(text, s):
    
    rez = ""
    for c in text:
        if c != " ":
            i = alphabet.find(c)
            i = (i + s ) % len(alphabet)
            rez=rez+alphabet[i]
        else:
             rez=rez+" "
    return rez


def decrypt(text, s):
    
    rez = ""
    for c in text:
        if c != ' ':
            i = alphabet.index(c)
            i = (i - s ) % len(alphabet)
            rez = rez + alphabet[i]
        else:
            rez = rez + " "
    return rez


in_str = input("Введите текст - ")
out_str = crypt(in_str, s)
print(out_str)
print(decrypt(out_str, s))
