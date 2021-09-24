from RobotArm import RobotArm

robotArm = RobotArm('exercise 2')

# Jouw python instructies zet je vanaf hier:
#    
robotArm.grab()
for right in range(9):
    robotArm.moveRight()
robotArm.drop()
for left in range(2):
    robotArm.moveLeft()
robotArm.grab()
for right2 in range(2):
    robotArm.moveRight()
robotArm.drop()    
for left2 in range(5):
    robotArm.moveLeft()
robotArm.grab()
for right3 in range(5):
    robotArm.moveRight()
robotArm.drop()        


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()