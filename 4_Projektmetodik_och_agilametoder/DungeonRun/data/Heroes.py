class Hero():

    def __init__(self):
        self.initiative = 1
        self.endurance = 1
        self.attack = 1
        self.agility = 1
        self.wealth = 0
        self.name = ""

    def special_ability(self):
        pass


class Warrior(Hero):

    def __init__(self):
        super().__init__()
        self.name = "Warrior"
        self.initiative = 5  # 5 default
        self.endurance = 9
        self.attack = 6
        self.agility = 4

    def shield_block(self):
        pass

    def __str__(self) -> str:
        return (
            f"Initiative:{self.initiative}Endurance{self.endurance}Attack:{self.attack}Agility{self.agility}Special ability:Shield block"
        )


class Wizard(Hero):

    def __init__(self):
        super().__init__()
        self.name = "Wizard"
        self.initiative = 6
        self.endurance = 4
        self.attack = 9
        self.agility = 5

    def blinding_light(self):
        pass

    def __str__(self) -> str:
        return (
            f"Initiative:{self.initiative}Endurance{self.endurance}Attack:{self.attack}Agility{self.agility}Special ability:Blinding light"
        )


class Thief(Hero):

    def __init__(self):
        super().__init__()
        self.name = "Thief"
        self.initiative = 7
        self.endurance = 5
        self.attack = 5
        self.agility = 7

    def critical_strike(self):
        pass

    def __str__(self) -> str:
        return (
            f"Initiative:{self.initiative}Endurance{self.endurance}Attack:{self.attack}Agility{self.agility}Special ability:Critical hit"
        )
