import sys
from robots import Robot

# Directions dictionary
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

# Begin user input at the start of the program and issues with user input
userCommand = input("Enter a command ")

if not userCommand.split()[0].upper() == 'PLACE':
    userCommand = input("Enter a command ")
    
else:
    userCoordinates = userCommand.split()[1].split(',')
    
    if int(userCoordinates[0]) < 0 or int(userCoordinates[0]) > 5 or int(userCoordinates[1]) < 0 or int(userCoordinates[1]) > 5:
        print("Coordinates must be between 0 and 5")
        sys.exit()

    if userCoordinates[2].upper() in directions:
        userRobot = Robot(userCoordinates[0], userCoordinates[1], userCoordinates[2].upper())
    else: 
        print("Direction is not valid")
        sys.exit()

# Once a new robot has been created move into user input loop
active = True

while active:
    action = input("")

    if action.upper().strip() == "REPORT":
        userRobot.report()
        active = False
    
    elif action.upper().strip() == "MOVE":
        userRobot.move()
    
    elif action.upper().strip() == "LEFT":
        userRobot.left()

    elif action.upper().strip() == "RIGHT":
        userRobot.right()

    else:
        print("Please enter a valid command")

sys.exit()