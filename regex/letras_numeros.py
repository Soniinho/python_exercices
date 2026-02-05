import re

def verifica_letras_numeros(string):
    # Define a expressão regular para letras e números apenas
    padrao = r'^[a-zA-Z0-9]+$'
    # Verifica se a string corresponde ao padrão
    if re.match(padrao, string):
        return True
    else:
        return False

# Exemplo de uso
string1 = "abc123"
string2 = "abc()ABC$123"  # Contém caracteres especiais
string3 = "123"      # Apenas números
string4 = "abcABC"      # Apenas letras

print(verifica_letras_numeros(string1))  # True
print(verifica_letras_numeros(string2))  # False
print(verifica_letras_numeros(string3))  # True
print(verifica_letras_numeros(string4))  # True
