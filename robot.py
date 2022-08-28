from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name= name
        self.health= 100
        self.active_weapon = Weapon("razor glove", 50)
                
    def robot_attack(self, amount_of_damage,active_weapon):
        print(f'{self.health} % health. ', self.name, 'the robot just attacked with ', {active_weapon}, '!')
        robot.health -= amount_of_damage
        print(f'{robot.health} % remains for ', robot.name)
        