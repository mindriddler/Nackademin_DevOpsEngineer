from datetime import timezone, datetime


class Statistics:
    def __init__(self):
        self.metrics = []

    def proccessed_trees(self):
        return len(self.metrics)

    def add_measurement(self):
        self.metrics.append(Measurement(1))


class Measurement:

    def __init__(self, value, type='generic') -> None:
        self.value = value
        self.type = type
        self.date = datetime.now(timezone.utc)
