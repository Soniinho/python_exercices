import threading

mutex = threading.Lock()
recurso_compartilhado = 0

def acessar_recurso(id):
    global recurso_compartilhado
    for i in range(10):
        with mutex:
            print(f"Thread {id} acessando recurso compartilhado: {recurso_compartilhado}")
            recurso_compartilhado += 1
            print(f"Thread {id} liberando recurso compartilhado: {recurso_compartilhado}")

if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=acessar_recurso, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
