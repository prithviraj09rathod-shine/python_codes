import threading


counter = 0
lock = threading.Lock()

def inc_fun():
    global counter
    for _ in range(10):
        lock.acquire()
        counter += 1
        lock.release()
def dec_fun():
    global counter
    for _ in range(5):
        lock.acquire()
        counter -= 1
        lock.release()

thread1= threading.Thread(target=inc_fun)
thread2= threading.Thread(target=dec_fun)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Final counter value:", counter)