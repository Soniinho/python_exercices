import random

def gerarTabelaSubst():
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alfabeto)
    return dict(zip('abcdefghijklmnopqrstuvwxyz', alfabeto))

def encriptar(msg, tabelaSubst):
    msgEncriptada = ''
    for char in msg:
        if char.isalpha():
            if char.islower():
                msgEncriptada += tabelaSubst[char]
            else:
                msgEncriptada += tabelaSubst[char.lower()].upper()
        else:
            msgEncriptada += char
    return msgEncriptada

def decriptar(msgEncriptada, tabelaSubst):
    tabelaDecript = {v: k for k, v in tabelaSubst.items()}
    msgDecriptada = ''
    for char in msgEncriptada:
        if char.isalpha():
            msgDecriptada += tabelaDecript[char.lower()]
        else:
            msgDecriptada += char
    return msgDecriptada

def main():
    tabelaSubst = gerarTabelaSubst()
    msg = input("Digite a mensagem: ")

    msgEncriptada = encriptar(msg, tabelaSubst)
    print("Mensagem criptografada:", msgEncriptada)

    msgDecriptada = decriptar(msgEncriptada, tabelaSubst)
    print("Mensagem descriptografada:", msgDecriptada)

if __name__ == "__main__":
    main()
