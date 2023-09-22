def encode(plainText, shift):
    result = ""
    for char in plainText:
        if char.isalpha():
            isUpper = char.isupper()
            char = char.lower()
            shiftedChar = chr((((ord(char)-ord("a"))+shift)%26)+ ord("a"))

            if isUpper:
                shiftedChar = shiftedChar.upper()
            result += shiftedChar
        else:
            result += char
    return(result)


def decode(cipherText, shift):
    result = ""
    for char in cipherText:
        if char.isalpha():
            isUpper = char.isupper()
            char = char.lower()
            unshifted = chr((((ord(char)-ord("a"))-shift)%26)+ ord("a"))
            if isUpper:
                unshifted = unshifted.upper()
            result += unshifted
        else:
            result += char
    return(result)

choice = input('''
What would you like to do?
1) Encode
2) Decode

(Input the corresponding number of the action)
''')

if choice == "1":
    plainText = input("Input the plain text")
    shift = int(input("Shift:"))
    cipher = encode(plainText, shift)
    print(f'''
Cipher Text:
{cipher}
          ''')

elif choice == "2":
    cipherText = input("Input cipher text")
    shift = int(input("Shift:"))
    plain = decode(cipherText, shift)
    print(f'''
Plain Text:
{plain}
          ''')

else:
    print("Not a choice")
