import threading

SIZE = 1000000
THREADS = 4

numeros = list(range(1, SIZE + 1))
resultados = [0] * THREADS

def soma_paralela(id):
    start = id * (SIZE // THREADS)
    end = (id + 1) * (SIZE // THREADS)
    soma = sum(numeros[start:end])
    resultados[id] = soma

if __name__ == "__main__":
    threads = []
    for i in range(THREADS):
        t = threading.Thread(target=soma_paralela, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    soma_total = sum(resultados)
    print(f"Soma total: {soma_total}")
