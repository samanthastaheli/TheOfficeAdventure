# CSE 210 final project Preparation and Planning

## 1. Decide on the game or interactive simulation you want to create.

### Game Inspo:
- Atari adventure
- Maze
- Super Mario bros but Star Wars like one on didj
- Dad and Adam’s game
- Escape room

### Favorite games:
- Halo
- Zelda
- Clue but lotr
- Catan but lotr

### Themes:
- Dinosaurs/science
- Lotr
- Star Wars
- Zelda
- Ready Player One
    - Find eggs
- The Office

### Idea: 
- adventure/escape room/clue lotr or Star Wars or ready player one theme

### Idea: The Office Adventure
- Adventure/Maze
    - Easter eggs??
    - Before each level show gif of funny scene in show that will be correlated to game level
    - Levels:
        - Dwight level: has to defeat certain things. Roy with pepper spray, Jim with snowballs
        - Michael level: Michael Scott paper company, holly sleeve of cardigan, run away from Jan, save Stanley
        - Jim: prank Dwight, propose to Pam
        - Pam: collect plants, answer phone (first level because just need to collect things)
        - Angela: save bandit

## 2. Create a list of the top priority ("must have") requirements for your program to be usable/playable.

- 1 level
- Actors:
    - 1 character from Office
    - Object to collect
    - Inventory to show collected objects
- Arrow controls move character
- Once character is near object. The object gets collected to inventory
- Collisions with walls makes actor not able to move through walls
- World seen on whole screen

## 3. Create a list of the lower priority ("nice to have") requirements that could take your program to the next level.

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

## 4. Create a list of all the classes you anticipate in your program. For each class, please state the things that class is responsible for.

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
