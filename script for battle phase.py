#The fight sequence scripted.
#This is what I am trying to accomplish.

#based on objects
Dname = 'Immovable' #passed_in_name
Dhealth = 100
Rhealth= 100
Rname = 'Irresistible' #passed_in_name'
Rweapon= 'force'

#battle_phase
while Dhealth > 0:
    #Dino_attack
    print(f'{Dname}, the dino, at {Dhealth}% health, just lashed {Rname}, the robot, with his tail!')
    Rhealth -= 40
    #Robot_attack
    print(f'''{Rname}, at {Rhealth} % remaining health, quickly retaliates upon {Dname} with the {Rweapon}!''')
    Dhealth -= 50

#declare_winner
print(f'{Dname}, at {Dhealth}% health, dies from injuries.',
Rname, 'survives as the winner.')

    

