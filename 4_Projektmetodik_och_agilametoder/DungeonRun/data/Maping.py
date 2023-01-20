import data.constants as const
from data.utilis import clear
from data.room_class import Room
from data.Heroes import Warrior, Wizard, Thief
from data.combat import Combat
from data.Monsters import Orc, Skeleton, GiantSpider, Troll
from random import choice


class Maping:

    def __init__(self,
                 width=0,
                 length=0,
                 x=0,
                 y=0,
                 map=[],
                 currpos=(0, 0),
                 hero="") -> None:
        self.hero = hero
        self.wealth = 0
        self.currpos = currpos
        self.width = width
        self.length = length
        self.size = None
        self.map = map
        self.x = x
        self.y = y
        self.lastcmd = None
        self.commands = {
            "left": self.moveleft,
            "right": self.moveright,
            "up": self.moveup,
            "down": self.movedown
        }

    def get_map_size(self):
        size_not_set = True

        while size_not_set:
            print("\nSmall = 4x4 rooms\n"
                  "Medium = 5x5 rooms\n"
                  "Large = 8x8 rooms\n")
            self.size = input(
                "What size map would you like to create? ").lower()
            if self.size == "small":
                self.width = 4
                self.length = 4
                return self.width, self.length, self.size
            elif self.size == "medium":
                self.width = 5
                self.length = 5
                return self.width, self.length, self.size
            elif self.size == "large":
                self.width = 8
                self.length = 8
                return self.width, self.length, self.size
            else:
                input("Invalid input. Please try again.\n"
                      "Press any key to continue.")
                continue

    def create_map(self):
        self.width, self.length, self.size = self.get_map_size()
        print(f"You have choosen to play on the {self.size} map.")
        print("Creating map.")
        self.map = [[self.gen_rooms() for i in range(self.width)]
                    for j in range(self.length)]
        return self.width, self.length, self.size, self.map

    def start_location(self):
        print("\nYour possible starting locations.\n"
              "Top left\n"
              "Top right\n"
              "Bottom left\n"
              "Bottom right\n")

        while True:
            start_pos = input("Where would you like to start?: ").lower()
            clear()
            print(const.TITLE)
            if start_pos == "top left":
                self.x = 0
                self.y = 0
                self.map = self.set_start_location()
                return self.map
            elif start_pos == "top right":
                self.x = self.width - 1
                self.y = 0
                self.map = self.set_start_location()
                return self.map
            elif start_pos == "bottom left":
                self.x = 0
                self.y = self.length - 1
                self.map = self.set_start_location()
                return self.map
            elif start_pos == "bottom right":
                self.x = self.width - 1
                self.y = self.length - 1
                self.map = self.set_start_location()
                return self.map
            else:
                print("That's not a valid starting location.")
                continue

    def set_start_location(self):
        if self.hero == "Warrior":
            self.hero = Warrior()
        elif self.hero == "Wizard":
            self.hero = Wizard()
        elif self.hero == "Thief":
            self.hero = Thief()
        self.currpos = (self.x, self.y)
        roomobj = self.map[self.y][self.x]
        roomobj.player = True
        for y in range(self.length):
            for x in range(self.width):
                self.map[y][x].populate()
        return self.map

    def set_exit_location(self):
        small_map = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 3), (2, 0),
                     (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
        medium_map = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 4),
                      (2, 0), (2, 4), (3, 0), (3, 4), (4, 0), (4, 1), (4, 2),
                      (4, 3), (4, 4)]
        large_map = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                     (0, 7), (1, 0), (1, 7), (2, 0), (2, 7), (3, 0), (3, 7),
                     (4, 0), (4, 7), (5, 0), (5, 7), (6, 0), (6, 7), (7, 0),
                     (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        if self.size == "small":
            small_map.remove((self.currpos[1], self.currpos[0]))
            exit_loc = choice(small_map)
            self.map[exit_loc[0]][exit_loc[1]].exit = True
        elif self.size == "medium":
            medium_map.remove((self.currpos[1], self.currpos[0]))
            exit_loc = choice(medium_map)
            self.map[exit_loc[0]][exit_loc[1]].exit = True
        elif self.size == "large":
            large_map.remove((self.currpos[1], self.currpos[0]))
            exit_loc = choice(large_map)
            self.map[exit_loc[0]][exit_loc[1]].exit = True
        self.map[exit_loc[0]][exit_loc[1]].loot = []
        self.map[exit_loc[0]][exit_loc[1]].lootvalue = 0
        self.map[exit_loc[0]][exit_loc[1]].skeleton = False
        self.map[exit_loc[0]][exit_loc[1]].orc = False
        self.map[exit_loc[0]][exit_loc[1]].troll = False
        self.map[exit_loc[0]][exit_loc[1]].spider = False

    def gen_rooms(self):
        x = Room()
        return x

    def drawmap(self):
        for row in self.map:
            print("|", end="")
            for i in row:
                print(i.__str__(), end="")
            print("|")

    def movement(self):
        while True:
            last_poss_y = self.currpos[1]
            last_poss_x = self.currpos[0]
            direction = input(
                "\nEnter a direction(Up, Down, Left or Right): ").lower()
            try:
                self.map[self.currpos[1]][self.currpos[0]].player = False
                self.map[self.currpos[1]][self.currpos[0]].visited = True
                self.map = self.commands[direction]()
                self.lastcmd = self.commands[direction]
                self.map[self.currpos[1]][self.currpos[0]].player = True
                print(self.map[self.currpos[1]][self.currpos[0]].loot)
            except IndexError:
                print("That's not a valid direction.")
            except KeyError:
                print("That's not a valid direction.")
            if self.map[self.currpos[1]][self.currpos[0]].exit:
                user_choice = input(
                    "You've found an exit, do you wish to leave the dungeon?(y/n):"
                )
                if user_choice.lower() == "y":
                    break
                elif user_choice.lower() == "n":
                    print("The journey continues!")
                else:
                    print("I take that as a no...")
            glory = self.docombat(last_poss_y, last_poss_x)
            if glory:
                self.wealth += self.map[self.currpos[1]][
                    self.currpos[0]].lootvalue
                if self.map[self.currpos[1]][self.currpos[0]].lootvalue > 0:
                    print(
                        f"You pick up {self.map[self.currpos[1]][self.currpos[0]].loot}, your total wealth is now {self.wealth}."
                    )
                self.map[self.currpos[1]][self.currpos[0]].lootvalue = 0
                self.map[self.currpos[1]][self.currpos[0]].loot = []
            elif glory == "dead":
                break
            self.drawmap()

    def docombat(self, y, x):
        if self.map[self.currpos[1]][self.currpos[0]].skeleton is True:
            combat = Combat(hero=self.hero, monster=Skeleton())
            combatresults = combat.odd_turns()
            if combatresults == "flee":
                self.flee(y, x, monster="skeleton")
                return False
            if combatresults == "dead":
                return "dead"
            elif combatresults == "victory":
                self.map[self.currpos[1]][self.currpos[0]].skeleton = False
                return True
        if self.map[self.currpos[1]][self.currpos[0]].orc is True:
            combat = Combat(hero=self.hero, monster=Orc())
            combatresults = combat.odd_turns()
            if combatresults == "flee":
                self.flee(y, x, monster="orc")
                return False
            if combatresults == "dead":
                return "dead"
            elif combatresults == "victory":
                self.map[self.currpos[1]][self.currpos[0]].orc = False
                return "victory"
        if self.map[self.currpos[1]][self.currpos[0]].troll is True:
            combat = Combat(hero=self.hero, monster=Troll())
            combatresults = combat.odd_turns()
            if combatresults == "flee":
                self.flee(y, x, monster="troll")
                return False
            if combatresults == "dead":
                return "dead"
            elif combatresults == "victory":
                self.map[self.currpos[1]][self.currpos[0]].troll = False
                return True
        if self.map[self.currpos[1]][self.currpos[0]].spider is True:
            combat = Combat(hero=self.hero, monster=GiantSpider())
            combatresults = combat.odd_turns()
            if combatresults == "flee":
                self.flee(y, x, monster="spider")
                return False
            if combatresults == "dead":
                return "dead"
            elif combatresults == "victory":
                self.map[self.currpos[1]][self.currpos[0]].spider = False
                return True
        else:
            return True

    def flee(self, last_poss_y, last_poss_x, monster):
        monster = monster
        self.map[self.currpos[1]][self.currpos[0]].monster = True
        self.map[self.currpos[1]][self.currpos[0]].player = False
        if self.lastcmd == self.moveleft:
            self.commands["right"]()
        elif self.lastcmd == self.moveright:
            self.commands["left"]()
        elif self.lastcmd == self.movedown:
            self.commands["up"]()
        elif self.lastcmd == self.moveup:
            self.commands["down"]()
        self.map[last_poss_y][last_poss_x].player = True
        self.map[last_poss_y][last_poss_x].visited = False
        self.drawmap()

    def exitmap(self):
        pass

    def moveleft(self):
        x = self.currpos[0]
        y = self.currpos[1]
        if x == 0:
            input(
                "You stumble into the wall.. I hope noone saw that!\nPress any key to continue.\n"
            )
            return self.map
        else:
            self.currpos = (x - 1, y)
            x = self.currpos[0]
            y = self.currpos[1]
            return self.map

    def moveright(self):
        x = self.currpos[0]
        y = self.currpos[1]
        if x == self.width - 1:
            input(
                "You stumble into the wall.. I hope noone saw that!\nPress any key to continue.\n"
            )
            return self.map
        else:
            self.currpos = (x + 1, y)
            x = self.currpos[0]
            y = self.currpos[1]
            return self.map

    def moveup(self):
        x = self.currpos[0]
        y = self.currpos[1]
        if y == 0:
            input(
                "You stumble into the wall.. I hope noone saw that!\nPress any key to continue.\n"
            )
            return self.map
        else:
            self.currpos = (x, y - 1)
            x = self.currpos[0]
            y = self.currpos[1]
            return self.map

    def movedown(self):
        x = self.currpos[0]
        y = self.currpos[1]
        if y == self.length - 1:
            input(
                "You stumble into the wall.. I hope noone saw that!\nPress any key to continue.\n"
            )
            return self.map
        else:
            self.currpos = (x, y + 1)
            x = self.currpos[0]
            y = self.currpos[1]
            return self.map

    def main(self):  # pragma: no cover
        print(const.TITLE)
        self.width, self.length, self.size, self.map = self.create_map()
        clear()
        print(const.TITLE)
        self.map = self.start_location()
        self.set_exit_location()
        self.drawmap()
        self.movement()
        self.exitmap()
        return self.wealth
