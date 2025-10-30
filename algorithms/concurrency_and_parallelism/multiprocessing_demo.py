from multiprocessing import Process
import time

def compute_square(n):
    print(f"Computing square of {n}")
    time.sleep(1)
    print(f"Result: {n * n}")

if __name__ == "__main__":
    numbers = [1, 2, 3]
    processes = [Process(target=compute_square, args=(n,)) for n in numbers]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
