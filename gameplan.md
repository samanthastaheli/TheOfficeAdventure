# Game Plan

## Idea: 
- adventure/escape room

## The Office Adventure
- Adventure/Maze
    - Easter eggs??
    - Before each level show gif of funny scene in show that will be correlated to game level
    - levels based on famous moments in show
    - Levels:
        - Dwight level: has to defeat certain things. Roy with pepper spray, Jim with snowballs
        - Michael level: Michael Scott paper company, holly sleeve of cardigan, run away from Jan, save Stanley
        - Jim: prank Dwight, propose to Pam
        - Pam: collect plants, answer phone (first level because just need to collect things)
        - Angela: save bandit

## Features

### High Priority 
- Actors:
    - 1 character from Office
    - Object to collect
    - Inventory to show collected objects
- Arrow controls move character
- Once character is near object. The object gets collected to inventory
- Collisions with walls makes actor not able to move through walls
- World seen on whole screen

### Lower Priority
- Explore world/not all of world shows on screen at once
- Gif shows on screen before level starts
- The Office set layout
- Multiple levels
- Main menu
    - Start
- Sub menu 
    - exit game
    - restart game
    - change level
- Once character is near object message shows up that user can press g key to grab object (g for grab)

### Basic classes for functionality or parent classes that are similar to batter programs:
- Director
- Actor
- Action
- Output service
- Input service
- Physics service
- Audio service
- Point

### Other child classes for more customization of game:
- Character
- Object
- Walls
