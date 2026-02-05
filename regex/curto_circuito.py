a = 5
b = 0

# Exemplo de curto-circuito com operador lógico AND (and)
if b != 0 and a / b > 2:
    print("Essa linha não será impressa.")
else:
    print("Não foi feita uma divisão por 0.")
