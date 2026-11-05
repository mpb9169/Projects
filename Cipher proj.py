def encrypt(plain_text, key):
    ciphertext = ""
    for char in plain_text:
        if char == " ":
            ciphertext += " "
        elif char.isalpha():
            shifted = (ord(char.upper()) - ord('A') + key) % 26
            ciphertext += chr(shifted + ord('A'))
    return ciphertext


def decrypt(ciphertext, key):
    plain_text = ""
    for char in ciphertext:
        if char == " ":
            plain_text += " "
        elif char.isalpha():
            shifted = (ord(char.upper()) - ord('A') - key) % 26
            plain_text += chr(shifted + ord('A'))
    return plain_text


# input from user
message = input("Enter a phrase/word: ")
key = int(input("Enter the shift key (number of shift): "))

encrypted = encrypt(message, key)
print(f"\nEncrypted: {encrypted}")

decrypted = decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

