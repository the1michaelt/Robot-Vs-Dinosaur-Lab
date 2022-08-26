from battlefield import Battlefield
from robot import Robot
from dinosaur import Dinosaur

game=Battlefield() #calling the function
game.run_game() #calling the element

robo_one = Robot("Freddee")
dino_one = Dinosaur("Jayzen", 50)


dino_one.attack(robo_one)
robo_one.attack(dino_one)

print(dino_one.attack)