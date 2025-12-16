import threading
def my_function():
    print("Thread started")
    print("Thread finished")
#create a thread 
thread = threading.Thread(target=my_function)
#start the thread
thread.start()
print('Main thread running')