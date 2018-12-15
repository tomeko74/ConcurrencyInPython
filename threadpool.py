from concurrent.futures import ThreadPoolExecutor
import threading

def task():
    print("Executing our task")
    result = 0
    i = 0
    for i in range(10):
        result = result + 1
    print("I: {}".format(result))
    print("Task Executed by {}".format(threading.current_thread()))

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        task1 = executor.submit(task)
        task2 = executor.submit(task)
        task3 = executor.submit(task)

if __name__ == '__main__':
    main()
    