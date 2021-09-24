from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

#Jouw python instructies zet je vanaf hier:
robotArm.speed = 5

eerste = 9
tweede = 8

for c in range(9):   
    robotArm.grab()
    color = robotArm.scan()
    if color == 'red':
        for a in range(eerste):
            robotArm.moveRight()
        robotArm.drop()        
        for b in range(tweede):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()
    eerste -= 1
    tweede -= 1    





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()