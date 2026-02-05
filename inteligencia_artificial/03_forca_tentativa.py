from pyswip import Prolog

def carregar_palavras(prolog, arquivo):
    with open(arquivo, 'r') as f:
        for linha in f:
            palavra = linha.strip().upper()
            prolog.assertz('palavra(\'{}\')'.format(palavra))

def escolher_palavra(prolog):
    q = prolog.query('palavra(X)')
    solucoes = list(q.solutions())
    q.close()
    if solucoes:
        return solucoes[0]['X']
    return None

def mostrar_palavra(palavra, letras_corretas):
    return ''.join(letra if letra in letras_corretas else '_' for letra in palavra)

def jogar_forca():
    prolog = Prolog()
    carregar_palavras(prolog, 'palavras.pl')

    palavra_secreta = escolher_palavra(prolog)
    letras_corretas = set()
    tentativas = 6

    print("Bem-vindo ao jogo de Forca!")
    print("Adivinhe a palavra secreta. Você tem {} tentativas.".format(tentativas))

    while tentativas > 0:
        print("\nPalavra: {}".format(mostrar_palavra(palavra_secreta, letras_corretas)))

        tentativa = input("Digite uma letra: ").strip().upper()

        if tentativa in palavra_secreta:
            letras_corretas.add(tentativa)
            if set(palavra_secreta) == letras_corretas:
                print("\nParabéns! Você ganhou! A palavra era '{}'.".format(palavra_secreta))
                break
        else:
            tentativas -= 1
            print("Letra incorreta. Você tem {} tentativas restantes.".format(tentativas))

    if tentativas == 0:
        print("\nVocê perdeu! A palavra secreta era '{}'.".format(palavra_secreta))

if __name__ == "__main__":
    jogar_forca()
