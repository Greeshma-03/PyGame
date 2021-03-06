# PyGame

## OverView
A 2D terminal game build in Python3 using the OOPS concept which is the simplified verison of the game Clash of clans


## Description of the game
This is Miniature version of Clash of clans where the user will control the king, move it up,down, forward and backward, while destroying buildings and fighting defences on the way.In this game the king and army of troops will try to destroy as many buildings as possible and collect the maximum amount of loot while doing so while the canons can reduce the health of king and troops when enetered in it's range.If King and army destroys all the buildings then we have won the game else if the king dies before destroying all the buildings then the user has lost the game.


## Rules and Functionalities

### King or Archer Queen
* To move the king left,right,up,down use the keys a,d,w,s respectively
* To attack TownHall or Townwalls or huts, press the space button 
* King can't cross the buildings or canons i.e the keys doesn't work when there are obstacles in the path
* King or Archer queen can't attack defensive buildings


### Canons
* Canons can attack king or troop when entered in it's zone that has predefined radius
* The canon decreases the health of king or troop by certain number of predefined damage points
* At a single point, the canon can only target only one troop irresepctive of number entered in it's zone


### Buildings
* Huts,Townwalls and Townhall need to be destroyed by the King and each of the buildings will have certain number of hitpoints with maximum points initially.
* The hitpoints are split into 3 ranges where each indicates:
  - Green - High strength,ranging from 50%-100%
  - Yellow - Average strength, ranging from 20%-50%
  - Red    - Low strength, ranging from 0%-10%
* The building vanishes when the hitpoints of that building drops to zero


### Barbarians
* The predefined spawning points has the keys 'N','K','G' where each troop comes upon clicking the respectives keys for each of the point.
* The health of each troop is indicated by it's color
* Maximum number of barbarians from one spawning point is 3


### Wizard Tower
* There should be at least two wizard towers in your village.
* The Wizard Tower can attack aerial troops.
* Range and damage are same as that of cannon.
* At a given point, the wizard tower can only target a single troop.
* The wizard tower deals AoE damage in a 3x3 tile area around the troop it is attacking.
* In case you have many troops stacked on one another, if the wizard tower were to target and attack one of them, all of them would take damage due to the AoE damage of the wizard tower.


### Levels
* Implemented a level system with three levels. For higher levels, the number of cannons and wizard towers should increase.
* Each level will inevitably have different layouts (due to the differing number of buildings). You are free to design the levels as you wish.The troop limit will reset for each level


## Features
* The health of the king is displayed as a health bar on top of the screen.
* Sound effects are added to the movements of the king and attack by the king
* Victory and Defeat are indicated at the end of each game.
* Replay feature for all possible attacks,is implemented and all the games played so far are availables as replay.
* The barbarian movement is automated and destroys the buildings and walls on it's way.
* The strength of building is represented by the color.


## Code Files
* game.py: The main infinite loop for taking input and calling corresponding functions defined in classes
* screen.py: Render the screen each time with colors of each entity involved in the game for small time step by clearing it and again displaying the board of the village
* king.py: The implementation of king moments and attacks are present in the file
* Barbarian.py: The implementation of automated moment of barbarian is coded here
* ballon.py: The implementation of automated moment of ballon is coded here
* archer.py: The implementation of automated moment of archer is coded here
* input.py: To wait for the input for every 0.1s and proceed next