import threading

THREADS = 4
barreira = threading.Barrier(THREADS)

def imprimir_numeros(id):
    print(f"Thread {id} iniciando execução")
    for i in range(1, 11):
        print(f"Thread {id}: {i}")
    print(f"Thread {id} esperando outras threads na barreira")
    barreira.wait()
    print(f"Thread {id} continuando execução após barreira")

if __name__ == "__main__":
    threads = []
    for i in range(THREADS):
        t = threading.Thread(target=imprimir_numeros, args=(i,))
        threads.append(t)
        t.start() 

    for t in threads:
        t.join()
