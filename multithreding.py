import threading
import time


def eatb():
    time.sleep(3)
    print("eat done")

def drink():
    time.sleep(4)
    print("drink done")

def study():
    time.sleep(5)
    print("study done")

x = threading.Thread(target=eatb, args=())
x.start()

y = threading.Thread(target=drink, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()
#eatb()
#drink()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())