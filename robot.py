from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name= name
        self.health= 100
        self.active_weapon = Weapon("razor glove", 50)
                
    def attack(self, dinosaur,active_weapon):
        # health = health - robot.attack_power
        print(robot.health)
        # print(f'''{robot.name} attacks with {robot.active_weapon}. ''')
