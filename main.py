import sys
from robots import Robot

# Directions and robots dictionaries
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
robots = []

# Function to create a new robot
def create_robot(user_input):
    if not user_input.split()[0].upper() == 'PLACE':
        userCommand = input("Enter a command ")
        
    else:
        userCoordinates = user_input.split()[1].split(',')
        
        if int(userCoordinates[0]) < 0 or int(userCoordinates[0]) > 5 or int(userCoordinates[1]) < 0 or int(userCoordinates[1]) > 5:
            print("Coordinates must be between 0 and 5")
            sys.exit()

        if userCoordinates[2].upper() in directions:
            robots.append(Robot(userCoordinates[0], userCoordinates[1], userCoordinates[2].upper()))

        else: 
            print("Direction is not valid")
            sys.exit()

# Begin user input at the start of the program and issues with user input
userCommand = input("Enter a command ")
create_robot(userCommand)

# Once a new robot has been created move into user input loop
active = True
activeRobot = robots[0]

while active:
    action = input("")

    if action.upper().strip() == "REPORT":
        activeRobot.report()
        print(f"Number of robots: {len(robots)}")
        active = False
    
    elif action.upper().strip() == "MOVE":
        activeRobot.move()
    
    elif action.upper().strip() == "LEFT":
        activeRobot.left()

    elif action.upper().strip() == "RIGHT":
        activeRobot.right()

    elif action.split()[0].upper() == "PLACE":
        create_robot(action)

    elif action.split()[0].upper() == "ROBOT":
        print("Change robot: todo")

    else:
        print("Please enter a valid command")

sys.exit()