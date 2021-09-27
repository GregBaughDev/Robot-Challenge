# Robot Challenge submission 

## Author 
Greg Baugh  

### Language
Python  

### Instructions
Commands are to be entered into the command prompt once the file is running.  
Download the main and robots .py files. From your command line run the following command:  
`python3 main.py`    
  
Start the programme with the `PLACE` command followed directly with x and y co-ordinates between 0 and 4 and a direction.
i.e. `PLACE 0,2,NORTH` or `PLACE 4,4,SOUTH`.  
  
You move the robot with the `MOVE` command and you change direction with either `LEFT` or `RIGHT`. You can add an extra robot by using the `PLACE` command above. You can switch between robots with the `ROBOT {NUMBER}` command. i.e. `ROBOT 2` will change to the second created robot.  
  
`REPORT` prints the current robots co-ordinates along with the current robot and number of active robots.  
  
### Tests
Test 1.  
`PLACE 0,0,NORTH`  
`MOVE`  
`MOVE`  
`RIGHT`  
`MOVE` 
`LEFT`
`MOVE`  
`REPORT`

* OUTPUT   
`1,3,NORTH`   
`Active robot: Robot 1`   
`Number of robots: 1`  

Test 2.  
`PLACE 4,3,NORTH`  
`MOVE`  
`MOVE`  
`RIGHT`  
`MOVE`  
`REPORT`  

* OUTPUT  
`4,4,EAST`  
`Active robot: Robot 1`  
`Number of robots: 1`  

Test 3.  
`PLACE 0,0,SOUTH`  
`MOVE`  
`RIGHT`  
`MOVE`  
`RIGHT`  
`MOVE`  
`PLACE 4,4,WEST`  
`ROBOT 2`  
`MOVE`  
`RIGHT`  
`MOVE`  
`ROBOT 1`  
`MOVE`  
`REPORT`  

* OUTPUT  
`0,2,NORTH`  
`Active robot: Robot 1`  
`Number of robots: 2`  

