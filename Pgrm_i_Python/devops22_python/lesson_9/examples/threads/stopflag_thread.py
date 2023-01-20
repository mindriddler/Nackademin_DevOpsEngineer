import threading
from time import sleep


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = False

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            sleep(1)
            print("working")


def main():
    mythread = MyThread()
    mythread.start()
    print(f"Is the thread alive: {mythread.is_alive()}")
    mythread.stop()
    mythread.join()
    print(f"Is the thread alive: {mythread.is_alive()}")
    print("Program exits")


if __name__ == '__main__':
    main()
