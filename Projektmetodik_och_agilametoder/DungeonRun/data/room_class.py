import data.Monsters
from data.loot_class import Loot
from random import randint


class Room():

    def __init__(self) -> None:
        self.visited = False
        self.player = False
        self.exit = False
        self.lootvalue = 0
        self.loot = []
        self.monsters = []
        self.skeleton = False
        self.orc = False
        self.troll = False
        self.spider = False

    def pop_loot(self):
        lt = Loot()
        for i in range(len(lt.loot_table)):
            success = self.rng(lt.loot_table[i][2])
            if success:
                self.loot.append(lt.loot_table[i][0])
                self.lootvalue = +lt.loot_table[i][1]

    def pop_monster(self):
        spiderchance = data.Monsters.GiantSpider().regularity
        orcchance = data.Monsters.Orc().regularity
        trollchance = data.Monsters.Troll().regularity
        skeletonchance = data.Monsters.Skeleton().regularity
        spidersucc = self.rng(spiderchance)
        if spidersucc:
            self.spider = True
            self.monsters.append(data.Monsters.GiantSpider().name)
        orcsucc = self.rng(orcchance)
        if orcsucc:
            self.orc = True
            self.monsters.append(data.Monsters.Orc().name)
        trollsucc = self.rng(trollchance)
        if trollsucc:
            self.troll = True
            self.monsters.append(data.Monsters.Troll().name)
        skeletonsucc = self.rng(skeletonchance)
        if skeletonsucc:
            self.skeleton = True
            self.monsters.append(data.Monsters.Skeleton().name)

    def rng(self, chance):
        roll = randint(0, 100)
        if roll <= chance:
            return True
        else:
            return False

    def populate(self):
        self.pop_loot()
        self.pop_monster()

    def __str__(self):
        if self.player:
            return "P"
        elif self.exit:
            return "E"
        else:
            if not self.visited:
                return "O"
            else:
                return "X"
