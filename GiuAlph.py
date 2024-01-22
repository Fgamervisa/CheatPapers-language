namee = {
    'a' : "_|",
    'b' : "|_",
    'c' : "-|",
    'd' : "|-",
    'e' : "v",
    'f' : ">",
    'g' : "^",
    'h' : "<",
    'i' : "_•|",
    'j' : "-•|",
    'k' : "|•_",
    'l' : "|•-",
    'm' : "•v",
    'n' : "•>",
    'o' : "^•",
    'p' : "<•",
    'q' : "U",
    'r' : "Ↄ",
    's' : "Ո",
    't' : "C",
    'u' : "•U",
    'v' : "•Ↄ",
    'w' : "•Ո",
    'x' : "C•",
    'y' : "•",
    'z' : "○",
    "'" : " ' " 
    } 

def encrypt(text):
    decrypted = []
    for char in text.lower():
        if char in namee.keys():
            decrypted.append(namee[char])
        else:
            decrypted.append(char)
    print(''.join(map(str, decrypted)))

# def decrypt_string(encrypted_string, decryption_dict):
    # decrypted_string = ''
    # for char in encrypted_string:
        # if char in decryption_dict:
            # decrypted_string += decryption_dict[char]
        # else:
            # decrypted_string += char
    # return decrypted_string

def main():
    text = input("Inserisci il testo ")
    encrypt(text)

main()

# def reverse():
#     reversed_namee = {
#     "_|" : 'a',
#     "|_" : 'b',
#     "-|" : 'c',
#     "|-" : 'd',
#     "v" : 'e',
#     ">" : 'f',
#     "^" : 'g',
#     "<" : 'h',
#     "_•|" : 'i',
#     "-•|" : 'j',
#     "|•_" : 'k',
#     "|•-" : 'l',
#     "•v" : 'm',
#     "•>" : 'n',
#     "^•" : 'o',
#     "<•" : 'p',
#     "U" : 'q',
#     "Ↄ" : 'r',
#     "Ո" : 's',
#     "C" : 't',
#     "•U" : 'u',
#     "•Ↄ" : 'v',
#     "•Ո" : 'w',
#     "C•" : 'x',
#     "•" : 'y',
#     "○" : 'z'
# }