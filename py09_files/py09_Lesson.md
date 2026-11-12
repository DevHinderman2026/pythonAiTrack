# py09 Lesson: Reading and Writing Files

You make three programs that use files. One reads data from a file instead of asking the user. One writes a report to a file. You also learn what to do when a file is missing, and how to put the date and time in a report.

## What to know

1. A text file holds lines of text. A CSV file is a text file where each line is one row of data and commas separate the columns. The first line is usually a header with the column names, like Name,Round1,Round2,Round3.
2. A relative path is just the file name, like scores.csv. It tells Python to look in the folder the program is running from. This keeps working if the folder is moved to another computer. A full path, like one that starts with C:, only works on the computer it was written on.
3. with open("scores.csv", "r") as file: opens the file for reading. The r means read. The lines indented under it can use the file. When the indented part ends, Python closes the file for you.
4. for line in file: reads the file one line at a time. Each line ends with a hidden new line character. line.strip() removes it.
5. To skip the header line, read one line before the loop starts with file.readline(), and do nothing with it.
6. line.split(",") breaks a line into a list at each comma. "Avery,88,92,79" becomes ["Avery", "88", "92", "79"]. The numbers are still strings, so they need int() before you can do math. parts[1:] is a slice of everything after the name.
7. A function can return two values at once: return names, scores. The line that calls it catches both, in the same order: names, scores = read_scores("scores.csv").
8. If a program tries to open a file that is not there, it crashes. os.path.exists("scores.csv") gives True if the file is there and False if it is not. The program can check first and print a message instead of crashing. This needs import os at the top.
9. open with "w" opens a file for writing. If the file is not there, it makes it. If it is there, it erases everything in it first. open with "a" adds to the end of the file instead of erasing it.
10. file.write("text\n") writes text to the file. write does not start a new line by itself, so you add the backslash n. print can also write to a file: print("text", file=out_file).
11. One function can print to the screen or to a file. Give it a parameter called out_file that starts as None. It uses print with file=out_file. If out_file is None, the text goes to the screen. If it is an open file, the text goes into the file.
12. To get the date and time, put from datetime import datetime at the top. datetime.now() gives the current date and time. .strftime("%Y-%m-%d %H:%M") turns it into text like 2026-11-12 08:15.

## Step 1. Set up

1. Tell Claude: "Make a folder called py09_files in my repository folder."
2. On GitHub, open py09_Questions.md in this lesson folder. Activate Download raw file. Do the same for scores.csv.
3. Tell Claude: "Move py09_Questions.md and scores.csv from my Downloads folder into my py09_files folder."
4. Tell Claude: "Read me scores.csv one line at a time." You should hear a header line and 5 players with 3 scores each.

## Step 2. First program: Scoreboard From a File

Tell Claude:

"Write a Python program called filescores.py and save it in my py09_files folder. Put a header comment at the top. It is the scoreboard from py08, but it reads the scores from scores.csv instead of asking for them. Copy in the total, sort, table, and analysis functions from my py08_nestedData scoreboard.py.

Write a function called read_scores that reads scores.csv with a relative path, skips the header line, and returns the list of names and the list of lists of scores.

If scores.csv is missing, print Error: could not find scores.csv and end without crashing.

Print Read, the number of players, and players from scores.csv, then a blank line, then the leaderboard table and the analysis.

Then write a file called report.txt. The first line is CLASS SCOREBOARD REPORT. The second line is Report created, then the date and time like 2026-11-12 08:15. Then the same table and analysis. Change the table and analysis functions so they can print to the screen or to a file. Print Report saved to report.txt at the end.

Use a main function. Give every function a comment. Put Input, Processing, and Output comments in main."

## Step 3. Run it

In the VS Code terminal, type: python filescores.py

You should hear Read 5 players from scores.csv. Then the table with Devon first at 292, then Avery, Casey, Blake, and Emery. Then Winner Devon, best single round Devon round 1 with 100, and highest scoring round Round 1 with an average of 84.00. Then Report saved.

Tell Claude: "Read me report.txt." It should have the title, the date and time, and the same table.

Now test the missing file. Tell Claude: "Rename scores.csv to scores_old.csv." Run the program. You should hear the error message, not a crash. Tell Claude to rename it back.

## Step 4. Explain

Tell Claude:

"Read me read_scores one line at a time. Then trace it for me with the line for Avery. Tell me what the line looks like after strip, after split, and after the numbers are turned into ints."

Then ask Claude:

"How does the program skip the header line?"

"How does one print_table function print to the screen and also to report.txt?"

"Why does the program use scores.csv and not a full path that starts with C?"

## Step 5. Break it on purpose

Tell Claude:

"In filescores.py, change the open for report.txt from w to a. Do not run it yet."

Before you run it, say what you think report.txt will look like if you run the program two times. Then run it two times, and have Claude read you report.txt. Ask Claude:

"Why does report.txt look like that? What is the difference between w and a?"

Tell Claude to change it back to w. Run it once and check report.txt again.

## Step 6. Two more programs

For each program, first say the plan: what file it reads or writes, what each line of the file holds, and what the program does with it. Then tell Claude to write it. Run it. Then ask Claude to walk you through the code.

1. inventory.py. First tell Claude: "Make a file called inventory.csv in my py09_files folder with a header line Item,Count and these lines: Pens,40 Pencils,25 Notebooks,12 Markers,18." Then have Claude write inventory.py. It reads inventory.csv, prints each item and its count, and prints the total count of all items. You should hear a total of 95. Then tell Claude to add the line Staplers,8 to inventory.csv. Run the program again without changing the code. You should hear a total of 103.

2. tracklist.py. It asks for 3 track names and writes them to a file called tracks.txt, one name per line, with a header line that says Track list and the date. Then it opens tracks.txt again, reads it, and prints every line with a number in front. Have Claude read you tracks.txt to check it.

For inventory.py, ask Claude: "Why did the program work with 5 items without any changes to the code?"

For tracklist.py, ask Claude: "Why does each write need a backslash n at the end?"

## Step 7. Make it yours

Have Claude make a CSV file of your releases, with a header line and columns for the title, the year, and the number of tracks. Then have it write a program that reads the file and prints the total number of tracks and the newest release. Before you run it, figure out the total yourself. Then run it and check.

## Step 8. Answer the questions

Open py09_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py09 files. Push.

## Turn in

All of these, pushed to your py09_files folder:

1. filescores.py, scores.csv, report.txt, inventory.py, inventory.csv, tracklist.py, tracks.txt, and your own program and CSV file
2. py09_Questions.md with your answers
