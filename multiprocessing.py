from multiprocessing import Process
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():

    print(multiprocessing.counter())

    a = Process(target=multiprocessing.counter, args=(10000000009))
    a.start()

    a.join()

    print("finnished in: ", time.perf_counter(), "second")

if __name__ == '__main__':
    main()