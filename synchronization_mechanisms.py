#synchronization mechanisms example
import threading
import time
#shared resource
counter = 0
#lock for synchronizing access to shared resource
lock = threading.Lock()
def increment_counter():
    global counter
    for _ in range(100000):
        #acquire the lock before accessing the shared resource
        lock.acquire()
        counter += 1
        #release the lock after accessing the shared resource
        lock.release()  
#creating threads
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)
#starting threads
thread1.start() 
thread2.start()
#waiting for threads to complete
thread1.join()
thread2.join()
print("Final counter value:", counter)
#without synchronization, the final counter value may be less than 200
#with synchronization, the final counter value should be exactly 200000
#this demonstrates basic synchronization using threading.Lock
#proper synchronization is crucial when multiple threads access shared resources
#improper synchronization can lead to race conditions

#other synchronization mechanisms include threading.RLock, threading.Semaphore,
#threading.Event, threading.Condition etc.
#the choice of synchronization mechanism depends on the specific use case
#always ensure to release locks in a finally block or use context managers  
