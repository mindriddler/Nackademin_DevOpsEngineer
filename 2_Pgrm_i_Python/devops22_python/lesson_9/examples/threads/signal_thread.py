from time import sleep
import threading
import signal
import sys


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    for t in threading.enumerate():
        if isinstance(t, MyThread):
            t.event.set()
            t.join()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


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
        if self.is_stopped():
            print(f"shutting down thread.. {self.name}")


def main():
    mythread = MyThread()
    mythread.start()
    print(f"Is the thread alive: {mythread.is_alive()}")
    mythread.join()
    print(f"Is the thread alive: {mythread.is_alive()}")
    print("Program exits")


if __name__ == '__main__':
    main()
