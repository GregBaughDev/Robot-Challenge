import sys
from robots import Robot

# Directions and robots dictionaries
directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']
robots = []

# Intro text
print("Welcome to 'Robot Challenge' by Greg Baugh")
print("Type 'QUIT' to quit")

# Function to create a new robot
def create_robot(user_input):
    if not user_input.split()[0].upper() == 'PLACE' or len(user_input.split()) != 2:
        print("Command must be in correct format")
        sys.exit()
        
    else:
        userCoordinates = user_input.split()[1].split(',')
        
        if int(userCoordinates[0]) < 0 or int(userCoordinates[0]) > 4 or int(userCoordinates[1]) < 0 or int(userCoordinates[1]) > 4:
            print("Coordinates must be between 0 and 4")
            sys.exit()

        if userCoordinates[2].upper() in directions:
            robots.append(Robot(userCoordinates[0], userCoordinates[1], userCoordinates[2].upper()))

        else: 
            print("Direction is not valid")
            sys.exit()

# Begin user input at the start of the program
userCommand = input("Enter a command - ")
create_robot(userCommand)

# Once a new robot has been created move into user input loop
active = True
activeRobot = robots[0]

while active:
    
    action = input("")

    if action.upper().strip() == "REPORT":
        activeRobot.report()
        print(f"Active robot: Robot {int(robots.index(activeRobot)) + 1}")
        print(f"Number of robots: {len(robots)}")
    
    elif action.upper().strip() == "MOVE":
        activeRobot.move()
    
    elif action.upper().strip() == "LEFT":
        activeRobot.left()

    elif action.upper().strip() == "RIGHT":
        activeRobot.right()

    elif action.split()[0].upper() == "PLACE":
        create_robot(action)

    elif action.split()[0].upper() == "ROBOT":
        newRobot = action.split(" ")[1]
        if int(newRobot) > len(robots):
            print(f"{int(newRobot)} isn't a valid robot")
        else:
            activeRobot = robots[int(newRobot) - 1]

    elif action.upper().strip() == "QUIT":
        active = False

    else:
        print("Please enter a valid command")  

sys.exit()