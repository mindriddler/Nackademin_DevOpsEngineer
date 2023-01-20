class Monster():

    def __init__(self):
        self.name = ""
        self.initiative = 0
        self.endurance = 0
        self.attack = 0
        self.agility = 0
        self.regularity = 0


class GiantSpider(Monster):

    def __init__(self):
        super().__init__()
        self.name = "Giant Spider"
        self.initiative = 7
        self.endurance = 1
        self.attack = 2
        self.agility = 3
        self.regularity = 20


class Skeleton(Monster):

    def __init__(self):
        super().__init__()
        self.name = "Skeleton"
        self.initiative = 4
        self.endurance = 2
        self.attack = 3
        self.agility = 3
        self.regularity = 15


class Orc(Monster):

    def __init__(self):
        super().__init__()
        self.name = "Orc"
        self.initiative = 6
        self.endurance = 3
        self.attack = 4
        self.agility = 4
        self.regularity = 10


class Troll(Monster):

    def __init__(self):
        super().__init__()
        self.name = "Troll"
        self.initiative = 2
        self.endurance = 4
        self.attack = 7
        self.agility = 2
        self.regularity = 5
