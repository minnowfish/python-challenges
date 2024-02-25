from english_words import get_english_words_set

def findPlainText(cipher):
    wordlist = get_english_words_set(['web2'], lower=True)
    
    max_score = 0 
    score = 0 
    best_shift = 0
    plaintext = ""

    for shift in range(26):
        decrypted = ""
        for char in cipher:
            if char.isalpha():
                if char.isupper():
                     decrypted += chr((((ord(char)-ord("A"))-shift)%26)+ ord("A"))
                else:
                     decrypted += chr((((ord(char)-ord("a"))-shift)%26)+ ord("a"))
            else:
                decrypted += char
        
        
        ValidWords = [word for word in decrypted.lower().split() if word in wordlist]
        score = len(ValidWords)

        if score > max_score:
            max_score = score
            best_shift = shift
            plaintext = decrypted
    return plaintext, best_shift
    
ciphertext = input("Cipher Text: ")
plaintext, shift = findPlainText(ciphertext)
if shift == 0:
    print("Unknown")
else:
    print(f"Plain Text: {plaintext} with shift {shift}")
