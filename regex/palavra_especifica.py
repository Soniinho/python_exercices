import re

texto = "O gato preto cruzou a rua rapidamente. O gato estava muito feliz pois a sua dona e seu amigo gato estavam do outro lado."

# Padrão que queremos encontrar
padrao = r"\bgato\b"

# Encontrar todas as ocorrências do padrão na string
ocorrencias = re.findall(padrao, texto)
#print("Ocorrências encontradas:", ocorrencias)

numero_ocorrencias = len(ocorrencias)
print("Número total de ocorrências encontradas:", numero_ocorrencias)
