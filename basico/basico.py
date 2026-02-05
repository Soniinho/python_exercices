codigo = int(input("Digite o código: "))

print(codigo)

if codigo > 16:
    print("Mais 16")
elif codigo > 12:
    print("Mais 12")
else:
    print("Menos 12")

for n in range(10):
    print(n)

for n in range(5, 10):
    print(n)

for n in range(10, 0, -1):
    print(n)

arquivo = open("arquivo.txt", 'w')
arquivo.write ('Curso Python \n')
arquivo.close

leitura=open('arquivo.txt', 'r')
print(leitura.read())
leitura.close()