LETTERS_EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()\""
LETTERS_GR = ""

class CeasarCipher():

    def encrypt(self, userInput,shift):
        encrypted = ""
        for i in userInput:
            index = LETTERS_EN.find(i)
            encrypted += LETTERS_EN[(index + shift) % len(LETTERS_EN)]
        return encrypted

    def decrypt(self, userInput, shift):
        decrypted = ""
        for i in userInput:
            index = LETTERS_EN.find(i)
            decrypted += LETTERS_EN[(index + shift) % len(LETTERS_EN)]
        return decrypted
       
def main():
    pass

if __name__ == "__main__":
    main()