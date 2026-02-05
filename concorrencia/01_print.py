import threading

def print_numbers(start):
    for i in range(start, start + 50):
        print(i, end=' ')

if __name__ == "__main__":
    start1 = 1
    start2 = 51
    t1 = threading.Thread(target=print_numbers, args=(start1,))
    t2 = threading.Thread(target=print_numbers, args=(start2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
