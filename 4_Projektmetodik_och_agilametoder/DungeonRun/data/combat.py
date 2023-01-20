from data.utilis import clear
import random
import data.constants as const


class Combat:

    def __init__(self, hero=None, monster=None) -> None:
        self.hero = hero
        self.monster = monster
        self.first_monster_attack = True
        clear()
        print(const.TITLE)
        print(f"You have encountered a {self.monster.name}!")

    def initiative(self):
        hero_initiative = 0
        for n in range(self.hero.initiative):
            hero_initiative += random.randint(1, 6)
        monster_initiative = 0
        for n in range(self.monster.initiative):
            monster_initiative += random.randint(1, 6)
        if hero_initiative >= monster_initiative:
            print(f"{self.hero.name} attacks first\n")
            return hero_initiative, monster_initiative
        else:
            print(f"{self.monster.name} attacks first\n")
            return hero_initiative, monster_initiative

    def combat_rolls_hero_monster(self):
        hero_attack = 0
        for n in range(self.hero.attack):
            hero_attack += random.randint(1, 6)
        monster_agility = 0
        for n in range(self.monster.agility):
            monster_agility += random.randint(1, 6)
        return hero_attack, monster_agility

    def combat_rolls_monster_hero(self):

        monster_attack = 0
        for n in range(self.monster.attack):
            monster_attack += random.randint(1, 6)
        hero_agility = 0
        for n in range(self.hero.agility):
            hero_agility += random.randint(1, 6)
        if self.hero.name == "Warrior" and self.first_monster_attack is True:
            hero_agility += 100
        return monster_attack, hero_agility

    def flee(self):
        if self.hero.name == "Wizard":
            flee_chance = 80
        else:
            flee_chance = self.hero.agility * 10
        flee_dice = random.randint(1, 100)
        if flee_dice <= flee_chance:
            print("You flee")
            return "flee"
        else:
            print("You tried to flee but didnt manage.")
            return

    def odd_turns(self):
        hero_initiative, monster_initiative = self.initiative()
        combat_ongoing = True

        while combat_ongoing:

            if hero_initiative >= monster_initiative:
                flee_or_attack = input("Flee or attack? ")
                if flee_or_attack == "attack":
                    hero_attack, monster_agility = self.combat_rolls_hero_monster(
                    )
                    if hero_attack >= monster_agility:
                        if self.hero.name == "Thief":
                            crit_chance = random.randint(1, 100)
                            if crit_chance >= 75:
                                self.monster.endurance -= 2
                                print(
                                    f"{self.hero.name} does a critical strike and deals 2 damage to {self.monster.name}"
                                )
                            else:
                                self.monster.endurance -= 1
                                print(
                                    f"{self.hero.name} attacks {self.monster.name} and deals 1 damage"
                                )
                        else:
                            self.monster.endurance -= 1
                            print(
                                f"{self.hero.name} attacks {self.monster.name} and deals 1 damage"
                            )
                        if self.monster.endurance <= 0:
                            print(f"{self.monster.name} is dead")
                            return "victory"
                            combat_ongoing = False
                        else:
                            combat_ongoing = self.even_turns(
                                hero_initiative, monster_initiative)
                            if self.hero.endurance <= 0:
                                return "dead"
                            else:
                                continue
                    else:
                        print(f"{self.hero.name} misses {self.monster.name}")
                        combat_ongoing = self.even_turns(
                            hero_initiative, monster_initiative)
                        if self.hero.endurance <= 0:
                            return "dead"
                        else:
                            continue
                elif flee_or_attack == "flee":
                    flee = self.flee()
                    if flee == "flee":
                        return "flee"
                    else:
                        combat_ongoing = self.even_turns(
                            hero_initiative, monster_initiative)
                        if self.hero.endurance <= 0:
                            return "dead"
                        else:
                            continue
            elif monster_initiative >= hero_initiative:
                flee_or_attack = input("Flee or attack? ")
                if flee_or_attack == "attack":
                    monster_attack, hero_agility = self.combat_rolls_monster_hero(
                    )
                    if monster_attack >= hero_agility:
                        self.hero.endurance -= 1
                        print(
                            f"{self.monster.name} attacks {self.hero.name} and deals 1 damage"
                        )
                        if self.hero.endurance == 0:
                            print(f"{self.hero.name} is dead")
                            return "dead"
                            combat_ongoing = False
                        else:
                            combat_ongoing = self.even_turns(
                                hero_initiative, monster_initiative)
                            if self.hero.endurance <= 0:
                                return "dead"
                            else:
                                continue
                    else:
                        if self.hero.name == "Warrior" and self.first_monster_attack is True:
                            print(
                                f"{self.monster.name} tried to attack but {self.hero.name} used special ability and dodge attack"
                            )
                            self.first_monster_attack = False
                            # self.hero.agility -= 100
                            combat_ongoing = self.even_turns(
                                hero_initiative, monster_initiative)
                            if self.hero.endurance <= 0:
                                return "dead"
                            else:
                                continue
                        else:
                            if monster_attack < hero_agility:
                                print(
                                    f"{self.monster.name} misses {self.hero.name}"
                                )
                            combat_ongoing = self.even_turns(
                                hero_initiative, monster_initiative)
                            if self.hero.endurance <= 0:
                                return "dead"
                            else:
                                continue
                elif flee_or_attack == "flee":
                    flee = self.flee()
                    if flee == "flee":
                        return "flee"
                    else:
                        combat_ongoing = self.even_turns(
                            hero_initiative, monster_initiative)
                        if self.hero.endurance <= 0:
                            return "dead"
                        else:
                            continue

    def even_turns(self, hero_initiative, monster_initiative):

        if hero_initiative <= monster_initiative:
            hero_attack, monster_agility = self.combat_rolls_hero_monster()
            if hero_attack >= monster_agility:
                if self.hero.name == "Thief":
                    crit_chance = random.randint(1, 100)
                    if crit_chance >= 75:
                        self.monster.endurance -= 2
                        print(
                            f"{self.hero.name} does a critical strike and deals 2 damage to {self.monster.name}"
                        )
                    else:
                        self.monster.endurance -= 1
                        print(
                            f"{self.hero.name} attacks {self.monster.name} and deals 1 damage"
                        )
                    if self.monster.endurance <= 0:
                        print(f"{self.monster.name} is dead")
                        return False
                    else:
                        return True
                else:
                    self.monster.endurance -= 1
                    print(
                        f"{self.hero.name} attacks {self.monster.name} and deals 1 damage"
                    )
                    if self.monster.endurance <= 0:
                        print(f"{self.monster.name} is dead")
                        return False
                    else:
                        return True
            else:
                print(f"{self.hero.name} misses {self.monster.name}")
                return True
        elif monster_initiative < hero_initiative:
            monster_attack, hero_agility = self.combat_rolls_monster_hero()
            if monster_attack >= hero_agility:
                self.hero.endurance -= 1
                print(
                    f"{self.monster.name} attacks {self.hero.name} and deals 1 damage"
                )
                if self.hero.endurance == 0:
                    print(f"{self.hero.name} is dead")
                    return False
                else:
                    return True
            else:
                if self.hero.name == "Warrior" and self.first_monster_attack is True:
                    print(
                        f"{self.monster.name} tried to attack but {self.hero.name} used special ability and dodge attack"
                    )
                    self.first_monster_attack = False
                    # self.hero.agility -= 100
                    return True
                else:
                    if monster_attack <= hero_agility:
                        print(f"{self.monster.name} misses {self.hero.name}")
                        return True
