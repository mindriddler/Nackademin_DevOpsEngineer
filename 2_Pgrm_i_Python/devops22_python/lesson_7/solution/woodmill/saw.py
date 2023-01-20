

class Saw:
    def __init__(self):
        self.running = False

    def connect_control_central(self, control_central):
        self.control_central = control_central

    def stop(self):
        self.running = False
        print("Saw closed")

    def start(self):
        self.running = True
        print("Saw started")

    def cut(self):
        if self.running and self.control_central:
            print("cutting logs into lumber")
            self.control_central.report_cut()
        else:
            print("sorry we are closed")
