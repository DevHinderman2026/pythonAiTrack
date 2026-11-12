# Terminal Guide

The terminal is where you run your Python programs. In VS Code, press Control plus backtick to open it. The backtick key is to the left of the 1 key.

You type a command and press Enter. The terminal runs it and shows the result on the next lines.

## Where am I

1. pwd tells you which folder you are in right now.
2. dir lists the files and folders in the folder you are in. ls does the same thing.

## Moving between folders

1. cd py02_variablesAndInput goes into that folder. Use the name of any folder that is inside the one you are in.
2. cd .. goes back up one folder, to the folder that holds the one you are in.
3. cd - goes back to the folder you were just in.
4. cd ~ goes to your home folder.

## Running programs

1. python --version checks that Python is installed. You should hear a version number.
2. python snack.py runs a program. The file has to be in the folder you are in. If you hear that the file cannot be found, use pwd and dir to check where you are.
3. Control plus C stops a program that is running. Use it when a program will not end, like an infinite loop.

## Keys that save typing

1. Up Arrow brings back the last command you typed. Press it again to go further back. Press Enter to run it again.
2. Down Arrow goes forward again through the commands you already typed.
3. Tab finishes a file or folder name for you. Type the first few letters, like cd py0, then press Tab. Press Tab again to go to the next name that matches.
4. Escape clears the command you are typing, so you can start over.
5. Home moves to the start of the line. End moves to the end of the line.
6. Control plus Left Arrow and Control plus Right Arrow move one word at a time in the line you are typing.

## Keeping the terminal tidy

1. cls clears the screen. clear does the same thing. Control plus L also works.
2. Control plus Shift plus backtick opens a new terminal.
3. exit closes the terminal.

## Reading the output

Alt plus F2 opens the terminal output as text you can move through with the arrow keys, one line at a time. Press Escape to go back to the terminal.

## A normal run

These commands go into a lesson folder, list the files, run the program, and go back up.

```text
pwd
cd py03_ifStatements
dir
python grades.py
cd ..
```

To run the same program again after you change it, press Up Arrow and then Enter.
