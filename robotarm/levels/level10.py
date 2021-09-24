from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

#Jouw python instructies zet je vanaf hier:
robotArm.speed = 1

eerst = 9
tweede = 8
for a in range(5):
    robotArm.grab()
    for b in range(eerst):
        robotArm.moveRight()
    robotArm.drop()  
    eerst -= 2      
    for c in range(tweede):
        robotArm.moveLeft()
    tweede -= 2    




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()