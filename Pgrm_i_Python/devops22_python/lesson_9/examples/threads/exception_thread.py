import threading
from time import sleep
from random import randint


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def randomly_fail(self):
        return randint(1, 100) > 70

    def run(self):
        while True:
            sleep(1)
            print("working")
            if (self.randomly_fail()):
                raise Exception("something failed")


def main():
    mythread = MyThread()
    mythread.start()
    print(f"Is the thread alive: {mythread.is_alive()}")
    mythread.join()
    print(f"Is the thread alive: {mythread.is_alive()}")
    print("Program exits")


if __name__ == '__main__':
    main()
