import random
import time
import os
import sys


class Monstera_Adasonii:
    def __init__(self, name, lightamount):
        self.name = name
        self.lightamount = lightamount
        self.age = 0
        self.support = False
        self.health = 100
        self.pests = False
        self.sickness = False
        self.needwatering = False
        self.wateramount = 80
        self.cycle = 0
        self.update()

    def water(self, amount):
        self.wateramount += amount 
        if self.wateramount > 40:
            self.needwatering = False
            print(f"{self.name} has been watered! {self.wateramount}% of water.")

    def relocate(self):
        choices = [100, 50, 30, 70, 0]
        choice = random.choice(choices)
        self.lightamount = choice
        print(f"{self.name} has moved to {choice}% amount of light.")

    def treat(self):
        if self.pests == True:
            choices = ["NeemOil", "Trap", "Pestacides"]
            choice = random.choices(choices)
            if choice == "[NeemOil]":
                self.pests = False
                self.health += 25
                print(f"{self.name} has been cured using Neem Oil!")
            if choice == "[Trap]":
                 self.pests = False
                 self.health += 10
                 print(f"{self.name} has been cured using a pest trap!")
            if choice == "[Pestacides]":
                self.pests = False
                self.health -= 15
                print(f"{self.name} has been cured using pestacides!")
                
        else:
            print("Theres nothing to cure!")
    
    def update(self):
        os.system("clear")
        self.cycle += 1
        self.wateramount -= 10
        if self.cycle == 6:
            self.cycle = 0
            self.age += 1
            print(f"{self.name} is now {self.age} years old!")
        if self.lightamount < 60:
            print(f"Give {self.name} more light!")
            self.health -= 5
        if self.lightamount > 100:
            print(f"{self.name} is getting to much light! lower its light.")
            self.health -= 10
        if self.wateramount < 40:
            self.needwatering = True
            print(f"{self.name} needs water!")
        if self.wateramount < 0 or self.wateramount == 0:
            print(f"{self.name} NEEDS water ASAP!")
            self.health -= 35
        if self.pests == True:
            print(f"{self.name} is being attacked by pests! treat it.")
            self.health -= 10
        if self.wateramount > 100:
            print(f"{self.name} is waterlogged! please stop watering.")
            self.health -= 15
        if self.health == 0 or self.health < 0 or self.age > 35:
            print(f"{self.name} has died :(")
            quit()
        pest = random.randint(1,100)
        if pest == 50:
            self.pests = True
        print("LEAF@ROOT V.1")
        print("Options \n 1: Water \n 2: Relocate \n 3: Treatment")
        option = input(": ")
        if option == "Water" or option == "water" or option == "1":
            amm = int(input("How much water?: "))
            self.water(amm)
            time.sleep(1)
            self.update()
        elif option == "Relocate" or option == "relocate" or option == "2":
            self.relocate()
            time.sleep(1)
            self.update()
        elif option == "Treat" or option == "Treat" or option == "Treatment" or option == "treatment" or option == "3":
            self.treat()
            time.sleep(1)
            self.update()
        

if __name__ == "__main__":
    nm = input("Whats your monstera's name?: ")
    lightam = int(input("How much light are you giving it?: "))
    pl = Monstera_Adasonii(nm, lightam)
    
        
    
    
        
