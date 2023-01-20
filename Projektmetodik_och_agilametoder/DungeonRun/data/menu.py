import json
import os
from time import sleep
from data.Maping import Maping
import data.constants as const
from data.utilis import clear


class Menu:

    def __init__(self):
        self.hero = ""
        self.hero_name = ""
        self.char_dict = {}
        self.char_name_list = []
        self.wealth = 0
        self.loot_value = 0  # self.update_wealth(name, self.loot_value) ?

    def menu_input(self):
        while True:
            try:
                user_input = int(input("> "))
                if user_input in range(1, 4):
                    return user_input
                else:
                    raise ValueError
            except ValueError:
                print("\r", end="Invalid input ")
                continue

    def write_json(self, new_data, filename=("char.json")):
        if os.path.exists(filename):
            with open(filename, 'r+') as file:
                file_data = json.load(file)
                file_data["Characters"].append(new_data)
                file.seek(0)
                json.dump(file_data, file, indent=4)
        else:
            new_json = {"Characters": []}
            with open(filename, 'w+') as file:
                new_json["Characters"].append(new_data)
                file.seek(0)
                json.dump(new_json, file, indent=4)

    def save_hero(self, hero_name, hero_choice):
        self.char_dict["Name"] = hero_name
        if hero_choice == 1:
            self.char_dict["Class"] = "Warrior"
            self.hero = "Warrior"
        if hero_choice == 2:
            self.char_dict["Class"] = "Wizard"
            self.hero = "Wizard"
        if hero_choice == 3:
            self.char_dict["Class"] = "Thief"
            self.hero = "Thief"
        self.char_dict["Wealth"] = 0

        self.write_json(self.char_dict)

    def create_hero(self):
        print(const.TITLE)
        print(const.HERO_CHOICE)
        hero_choice = self.menu_input()
        clear()
        print(const.TITLE)
        print(const.HERO_NAME)
        while True:
            self.hero_name = input("> ").capitalize()
            if self.hero_name in self.char_name_list:
                print("That name is already taken.")
                continue
            else:
                self.save_hero(self.hero_name, hero_choice)
                clear()
                break
        self.correct_values(self.hero_name)

    def load_existing(self):
        if os.path.exists("char.json"):
            file = open("char.json")
            data = json.load(file)
            for character in data["Characters"]:
                self.char_name_list.append(character["Name"])
            return data
        else:
            pass

    def load_char(self):
        data = self.load_existing()
        while True:
            if not data:
                print("No existing characters, create one ...")
                sleep(1.5)
                clear()
                self.create_hero()
                break
            else:
                print(const.TITLE)
                for character in data["Characters"]:
                    chars = (
                        f'{str(character["Name"]).ljust(10)[:10]}'
                        f'{str(character["Class"]).ljust(10)[:10]}'
                        f'Wealth: {str(character["Wealth"]).ljust(10)[:10]}')
                    self.hero = character["Class"]
                    print(chars.center(100))
                self.hero_name = input("Choose character: ").capitalize()
                if self.hero_name in self.char_name_list:
                    clear()
                    self.correct_values(self.hero_name)
                    break
                else:
                    print("That character doesn't exist.")
                    sleep(1.5)
                    clear()
                    continue
                    # Go back to menu?

    def correct_values(self, name):
        data = self.load_existing()
        for character in data["Characters"]:
            if name == character["Name"]:
                self.hero = character["Class"]
                self.wealth = character["Wealth"]
                break

    def update_wealth(self, name, loot_value):
        data = self.load_existing()
        self.char_name_list = data["Characters"]
        list_index = next((index
                           for (index, d) in enumerate(self.char_name_list)
                           if d["Name"] == name), None)

        wealth_update = loot_value + self.wealth
        self.char_dict["Wealth"] = wealth_update

        data['Characters'][list_index]['Wealth'] = wealth_update
        self.wealth = wealth_update
        with open("char.json", 'w+') as file:
            json.dump(data, file, indent=4)

    def run(self):
        self.load_existing()
        print(const.TITLE)
        print(const.PRESS)
        input()
        clear()
        self.running = True
        while self.running:
            print(const.TITLE)
            print(const.MAIN)
            choice = self.menu_input()
            clear()
            if choice == 1:
                self.create_hero()
                self.loot_value = Maping(hero=self.hero).main()
                self.update_wealth(self.hero_name, self.loot_value)
            elif choice == 2:
                self.load_char()
                self.loot_value = Maping(hero=self.hero).main()
                self.update_wealth(self.hero_name, self.loot_value)
            elif choice == 3:
                break
