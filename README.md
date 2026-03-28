# Game-notes-tracker-
A basic intelligent system that organizes and retrieves game-related information to improve continuity in gameplay.
----------Project Title--------------
Game Notes Tracker

Name: Eshita Parihar

----------Key Contents--------------
Introduction

Features

Installation

Usage

Workflow

PseudoCode

----------Introduction--------------
This project is a Game Notes Tracker designed to help players store and manage important information related to games. It allows users to save details such as controls, objectives, and progress so that they can easily continue playing after taking a break.

In many cases, players forget key information when they return to a game after some time. This leads to confusion and interrupts the gaming experience. This project provides a simple solution by organizing and storing game-related notes in a structured way.

The system is built using Python and focuses on ease of use. It helps reduce frustration and allows users to resume gameplay without needing to restart or spend time figuring things out again.

----------Features--------------
Add Game Notes
Allows users to enter a game name and store details like controls, objectives, and progress.

View Notes
Lets users retrieve saved information for any game.

Update Notes
Users can modify existing notes as their progress changes.

Persistent Storage
All data is saved in a JSON file so that it is not lost after closing the program.

Simple Interface
Provides a menu-driven command-line interface that is easy to use.

----------Installation--------------
Follow the steps below to set up the Game Notes Tracker:

Install Python
Make sure Python (version 3.x) is installed on your system.

Download the Project Files
Place the following files in one folder:

main.py

game_notes.json (will be created automatically if not present)

Run the Program
Open a terminal or command prompt and run:

python main.py

The program will start and create the data file if needed.

----------Usage--------------
To use the Game Notes Tracker:

Run the Program
Open the terminal and execute:

python main.py

Main Menu Options
The system displays a menu with options:

1 Add Notes
2 View Notes
3 Exit

Using the Features

a) Add Notes
Enter the game name
Enter controls
Enter current objective
Enter progress details
The notes are saved automatically

b) View Notes
Enter the game name
The system displays saved details

c) Exit
Closes the program safely

----------Workflow--------------
START
Load existing data from JSON file

Display main menu
User selects an option

If Add Notes
→ Take input
→ Store data
→ Save file

If View Notes
→ Search for game
→ Display stored data

If Exit
→ End program

----------PseudoCode--------------
START

LOAD data from JSON file

REPEAT
DISPLAY menu

```
INPUT choice  

IF choice == 1 THEN  
    INPUT game name  
    INPUT controls  
    INPUT objectives  
    INPUT progress  
    STORE data  
    SAVE file  

ELSE IF choice == 2 THEN  
    INPUT game name  
    IF found THEN  
        DISPLAY notes  
    ELSE  
        DISPLAY "No data found"  
    ENDIF  

ELSE IF choice == 3 THEN  
    EXIT  

ELSE  
    DISPLAY "Invalid choice"  
```

END REPEAT

SAVE data

END

About
A simple CLI tool to store and manage game controls, objectives, and progress so players can easily continue gameplay after a break.

