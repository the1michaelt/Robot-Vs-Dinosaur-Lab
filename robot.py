from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name= name
        self.health= 100
        self.has_weapon= Weapon('Force', 25) #weapon is instantiated here. Pass in the name and attack power as the two arguments

    def attack(self, dinosaur):
        dinosaur.health -= self.has_weapon.attack_power
        print(f'''{self.name}, the robot, compels {dinosaur.name} with {self.has_weapon.name}! {dinosaur.name}'s health drops to {dinosaur.health}.''') #two dot-notations to invoke an instance variable of an object e.g., self.has_weapon.name