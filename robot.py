from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name= name
        self.health= 100
        self.active_weapon = Weapon("force", 50)
                
    def robot_attack(self, amount_of_damage,active_weapon):
        robot.health -= amount_of_damage
        print(f'''{robot.name}, at {robot.health} % remaining health, quickly retaliates upon {dinosaur.name} with the {robot.active_weapon}!''')
        