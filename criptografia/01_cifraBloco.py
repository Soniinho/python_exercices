def encriptarBloco(bloco, chave):
    blocoCifrado = ""
    for char in bloco:
        blocoCifrado += chr(ord(char) ^ chave)
    return blocoCifrado

def decriptarBloco(blocoCifrado, chave):
    blocoDecifrado = ""
    for char in blocoCifrado:
        blocoDecifrado += chr(ord(char) ^ chave)
    return blocoDecifrado

def msgCifrar(msg, blocoTam, chave):
    blocosCifrados = []
    for i in range(0, len(msg), blocoTam):
        bloco = msg[i:i+blocoTam]
        blocoCifrado = encriptarBloco(bloco, chave)
        blocosCifrados.append(blocoCifrado)
    return ''.join(blocosCifrados)

def msgDecifrar(msgCifrada, blocoTam, chave):
    msgDecifrada = ""
    for i in range(0, len(msgCifrada), blocoTam):
        blocoCifrado = msgCifrada[i:i+blocoTam]
        blocoDecifrado = decriptarBloco(blocoCifrado, chave)
        msgDecifrada += blocoDecifrado
    return msgDecifrada

mensagem_original = "Biscoito de Polvilho"
tamanho_bloco = 8
chave = 42

# a criptografia está criando \ e caracteres de escape na string

mensagem_criptografada = msgCifrar(mensagem_original, tamanho_bloco, chave)
# print("Mensagem criptografada:", mensagem_criptografada.replace("\n", "\\n"))
print("Mensagem criptografada:", mensagem_criptografada.encode('unicode_escape').decode())

mensagem_descriptografada = msgDecifrar(mensagem_criptografada, tamanho_bloco, chave)
print("Mensagem descriptografada:", mensagem_descriptografada)