
from threading import Thread, enumerate
from time import sleep


class Client(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.running = True

    def run(self):
        while self.running:
            sleep(1)
            print("working.... zzzZZZz")


Client().start()
Client().start()

for thread in enumerate():
    if isinstance(thread, Client):
        thread.running = False
        print(thread)
