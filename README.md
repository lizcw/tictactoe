# TicTacToe Board Calculator
A program that can examine a given TicTacToe board and determine if the board is valid, whether the game
is over, and if it is over whether X or O won.

## Rules of the game

Note that X always goes first.

The program will take input from the command line where a board is represented over 3 lines like:

```
X X
OOO
X
```
where X and O represent the players moves and <space> represents an unfilled cell.

The output should be one of:

+ X Wins!
+ O Wins!
+ Draw
+ Game Incomplete
+ Invalid Game
+ Invalid Input

## Development Notes

I have used a standard MVC structure with command line input (which could be replaced by a GUI) in Python v3.6.4.  
Installed packages are listed with versions in requirements.txt.
  
To set up the python environment (assuming Python 3.6.4 is installed), from required location:
1. virtualenv tenv 
1. cd tenv
1. [WINDOWS] Scripts\activate.bat
1. [MAC or LINUX] bin/activate

To run the program (once the virtual env is activated)
1. cd <PROJECT DIRECTORY>
1. pip -r requirements.txt
1. python run.py

*Developed by Liz Cooper-Williams for DoseMe*
