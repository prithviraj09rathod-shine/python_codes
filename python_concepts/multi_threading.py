#multithreading example
import threading
import time
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)   

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(letter)
        time.sleep(1)   
#creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
#starting threads
thread1.start()
thread2.start() 
#waiting for threads to complete
thread1.join()
thread2.join()  
print("Finished executing both threads")
#main thread
print("Main thread continues execution")
#output will show numbers and letters printed in an interleaved manner
#indicating that both threads are running concurrently
#each thread sleeps for 1 second after printing each item
#so total time will be around 5 seconds instead of 10 seconds if run sequentially
print("Main thread finished execution")
#thread1 and thread2 are child threads created by the main thread
#main thread waits for both child threads to complete using join()
#once both threads complete, main thread resumes and prints final message
#this demonstrates basic multithreading in Python using threading module

#threads share the same memory space, so they can access shared data
#but proper synchronization is needed when accessing shared data to avoid
#race conditions.In this example, there is no shared data, so no synchronization is needed
 
#for more complex scenarios, threading locks or other synchronization
#mechanisms may be needed to ensure thread safety when accessing shared data
#also note that Python's Global Interpreter Lock (GIL) can limit true
#parallelism in CPU-bound tasks, but for I/O-bound tasks, multithreading
#can still provide performance improvements by allowing other threads
#to run while one thread is waiting for I/O operations to complete
#for CPU-bound tasks, multiprocessing module can be used to achieve
#true parallelism by creating separate processes with their own
#memory space