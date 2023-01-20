from stats import Statistics
from saw import Saw


class ControlCentral:

    def __init__(self, saw=Saw()):
        self.stats = Statistics()
        self.saw = saw
        self.saw.connect_control_central(self)

    def status(self):
        processed_trees = self.stats.proccessed_trees()
        return {'running': self.saw.running, 'processed_trees': processed_trees}

    def report_cut(self):
        self.stats.add_measurement()

    def stop(self):
        self.saw.stop()

    def start(self):
        self.saw.start()
