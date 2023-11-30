UPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"

def encrypt(userInput,shift):
    encrypted = ""
    for i in userInput:
        if i.isupper() == True:
            index = UPERCASE.find(i)
            encrypted += UPERCASE[index + shift]
        if i.islower() == True:
            index = LOWERCASE.find(i)
            encrypted += LOWERCASE[index + shift]
    return encrypted

def decrypt(userInput, shift):
    decrypted = ""
    for i in userInput:
        if i.isupper():
            index = UPERCASE.find(i)
            decrypted += UPERCASE[index - shift]
        if i.islower():
            index = LOWERCASE.find(i)
            decrypted += LOWERCASE[index - shift]
    return decrypted
            
def main():
    encrypted = encrypt("test", 2)
    decrypted = decrypt("vguv",2)
    print(encrypted," ",decrypted)
    
if __name__ == "__main__":
    main()
