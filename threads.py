import threading


def myTask():
    print("Hell world: {}".format(threading.current_thread()))


myThread = threading.Thread(target=myTask)
myThread.start()
