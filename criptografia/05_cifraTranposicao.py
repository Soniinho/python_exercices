import math

chave = "2314"

def msgEncriptada(msg):
    msgEncriptada = ""

    indexChave = 0

    msgTam = float(len(msg))
    msgLista = list(msg)
    chaveLista = sorted(list(chave))

    coluna = len(chave)

    linha = int(math.ceil(msgTam / coluna))

    encherNada = int((linha * coluna) - msgTam)
    msgLista.extend("_" * encherNada)

    matriz = [msgLista[i : i + coluna] for i in range(0, len(msgLista), coluna)]

    for _ in range(coluna):
        indexAtual = chave.index(chaveLista[indexChave])
        msgEncriptada += "".join([linha[indexAtual] for linha in matriz])
        indexChave += 1

    return msgEncriptada


def decryptMessage(cipher):
    msgDecriptada = ""

    indexChave = 0

    indexMsg = 0
    msgTam = float(len(cipher))
    msgLista = list(cipher)

    coluna = len(chave)

    linha = int(math.ceil(msgTam / coluna))

    chaveLista = sorted(list(chave))

    matrizCifra = []
    for _ in range(linha):
        matrizCifra += [[None] * coluna]

    for _ in range(coluna):
        indexAtual = chave.index(chaveLista[indexChave])

        for j in range(linha):
            matrizCifra[j][indexAtual] = msgLista[indexMsg]
            indexMsg += 1
        indexChave += 1

    try:
        msgDecriptada = "".join(sum(matrizCifra, []))
    except TypeError:
        raise TypeError("Esse programa não", "pode com palavras repetidas.")

    contarNull = msgDecriptada.count("_")

    if contarNull > 0:
        return msgDecriptada[:-contarNull]

    return msgDecriptada

msg = "Biscoito de polvilho"
print("Mensagem usada: {}".format(msg))

cifra = msgEncriptada(msg)
print("Mensagem Encriptada: {}".format(cifra))

print("Mensagem Decriptada: {}".format(decryptMessage(cifra)))
