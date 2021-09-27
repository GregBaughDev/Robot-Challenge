# Robot Challenge submission 

## Author 
Greg Baugh  

### Language
Python  

### Instructions
Commands are to be entered into the command prompt once the file is running.  
Download the main and robots .py files. From your command line run the following command:  
`python3 main.py`

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
`Activev robot: Robot 1`  
`Number of robots: 2`  

