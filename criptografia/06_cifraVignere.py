def encriptar(msg, chave):
    msgEncriptada = ""
    chaveTam = len(chave)
    for i in range(len(msg)):
        char = msg[i]
        if char.isalpha():
            troca = ord(chave[i % chaveTam].lower()) - ord('a')
            if char.islower():
                msgEncriptada += chr((ord(char) - ord('a') + troca) % 26 + ord('a'))
            else:
                msgEncriptada += chr((ord(char) - ord('A') + troca) % 26 + ord('A'))
        else:
            msgEncriptada += char
    return msgEncriptada

def decriptar(msgEncriptada, chave):
    msgDecriptada = ""
    chaveTam = len(chave)
    for i in range(len(msgEncriptada)):
        char = msgEncriptada[i]
        if char.isalpha():
            troca = ord(chave[i % chaveTam].lower()) - ord('a')
            if char.islower():
                msgDecriptada += chr((ord(char) - ord('a') - troca + 26) % 26 + ord('a'))
            else:
                msgDecriptada += chr((ord(char) - ord('A') - troca + 26) % 26 + ord('A'))
        else:
            msgDecriptada += char
    return msgDecriptada

def main():
    msg = input("Digite o texto a ser criptografado: ")
    chave = input("Digite a chave: ")

    msgEncriptada = encriptar(msg, chave)
    print("Texto criptografado:", msgEncriptada)

    msgDecriptada = decriptar(msgEncriptada, chave)
    print("Texto descriptografado:", msgDecriptada)

if __name__ == "__main__":
    main()
