class Dinosaur:
    def __init__(self, name, attack_power=25): #self here is always the first argument
        self.name= name
        self.health =100
        self.attack_power = attack_power

    def attack(self, robot): #the attack is narrative: announcement of the event and the reduction of health
        robot.health -=self.attack_power #pass in the robot health minus the value of attack power; integer to integer
        print(f'''{self.name}, the dinosaur, withstands {robot.name}! {robot.name}'s health plunges to {robot.health}.''') #robot, the opponent, is not the object of self

