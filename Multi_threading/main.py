#multithreading
import threading
import time

def task_1():
    print('Task 1 started')
    time.sleep(2)
    print('Task 1 completed')


def task_2():
    print('Task 2 started')
    time.sleep(1)
    print('Task 2 completed')    


t1= threading.Thread(target=task_1)    
t2= threading.Thread(target=task_2)  

t1.start()
t2.start()
#wait for the threads to complete
t1.join()
t2.join()
print('Both tasks completed')

