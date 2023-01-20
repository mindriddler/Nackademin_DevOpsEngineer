import threading
from time import sleep


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def stop(self):
        self.event.set()

    def is_stopped(self):
        return self.event.is_set()

    def run(self):
        while not self.is_stopped():
            sleep(1)
            print("working")


def main():
    mythread = MyThread()
    mythread.start()
    print(f"Is the thread alive: {mythread.is_alive()}")
    # mythread.stop()
    mythread.event.set()
    mythread.join()
    print(f"Is the thread alive: {mythread.is_alive()}")
    print("Program exits")


if __name__ == '__main__':
    main()
