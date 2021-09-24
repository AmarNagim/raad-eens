from RobotArm import RobotArm
import time

robotArm = RobotArm()
robotArm.randomLevel(1,7)

#Jouw python instructies zet je vanaf hier:
times = 1
robotArm.speed = 1

grabSpeed = robotArm.grab()
while grabSpeed == True:
    for b in range(times):
        robotArm.moveRight()
    robotArm.drop()
    for c in range(times):
        robotArm.moveLeft()
    grabSpeed = robotArm.grab()        
    times += 1


        
    
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()