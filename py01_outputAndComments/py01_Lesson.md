# py01 Lesson: Printing and Comments

In this track you make Python programs by telling Claude what to build. You do not need to type the code. Your job is to understand it: what each line does, what order it runs in, and why the output comes out the way it does.

In this lesson you make three programs that print text on the screen. Then you answer the questions in py01_Questions.md and push your answers to GitHub with your programs.

## What to know

1. A Python program is a text file whose name ends in .py. Python reads it from the top line to the bottom line and does what each line says, in that order.
2. print shows text on the screen. The text goes inside the parentheses, inside quote marks. Each print starts a new line.
3. A comment is a line that starts with a pound sign. Python skips comments. They are notes for people who read the code.
4. A header comment goes at the top of every program. It has your name, the date, the program name, and a one-line description. It tells anyone who opens the file who wrote the program and what it is supposed to do, before they read any code.
5. Comments that say Input, Processing, or Output above a group of lines tell the reader what that part of the program does. They make a program easier to follow.
6. A syntax error means Python could not understand a line. When that happens, none of the program runs, not even the lines that were fine.

## Step 1. Set up

1. Tell Claude: "Make a folder called py01_outputAndComments in my repository folder."
2. On GitHub, open py01_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py01_Questions.md from my Downloads folder into my py01_outputAndComments folder."

## Step 2. First program: Game Night Welcome

Tell Claude:

"Write a Python program called welcome.py and save it in my py01_outputAndComments folder. Put a header comment at the top with my name, today's date, the program name, and a one-line description. Put a comment that says Output above the print lines. The program prints this:

A line of 30 equal signs.
MCCC GAME NIGHT, with 3 spaces in front.
Friday, 6:00 PM - Room 112, with 3 spaces in front.
Another line of 30 equal signs.
Events tonight:
Three numbered events, each with 2 spaces in front: Board Games, Video Game Tournament, Trivia.
Bring a friend!

Use the equal sign times 30 for the lines of equal signs. Print at least two of the lines with one print statement and a new line code."

## Step 3. Run it

1. Open VS Code. Open your py01_outputAndComments folder.
2. Press Control plus backtick to open the terminal.
3. Type: python welcome.py
4. Press Enter and listen to the output. It should match the list in Step 2.

If you hear an error instead, tell Claude the error message. Have it fix the file, then run it again.

## Step 4. Explain

Tell Claude:

"Read me welcome.py one line at a time. After each line, tell me in one short sentence what it does. Tell me which lines Python skips."

Then ask Claude:

"What does the backslash n do inside the quote marks?"

"Why does the equal sign times 30 make a line of 30 equal signs?"

"What is the difference between a comment and a print line? Which one shows up when the program runs?"

## Step 5. Break it on purpose

Tell Claude:

"In welcome.py, remove the closing quote mark from the Bring a friend line. Save it."

Run it. Listen to the error. Ask Claude:

"What does this error mean? Which line number does it point to? Did any of the program run?"

Then tell Claude to put the quote mark back. Run it again to make sure it works.

## Step 6. Two more programs

For each program below, first say the plan out loud or in a note: what gets printed, in what order. Then tell Claude to write it. Run it. Then ask Claude to walk you through the code.

1. schedule.py. A daily schedule card for the IT Academy. A line of 34 stars at the top and after the title. Two title lines: MEDINA COUNTY CAREER CENTER, and IT Academy - Daily Schedule. Then six times and classes: 7:30 Homeroom, 7:45 Software Engineering Lab, 10:15 Break, 10:30 Software Engineering Lab, 12:15 Lunch, 12:45 Academics. Then a line of 34 dashes. The last line is: Room 112 - "Bring your laptop!" with the quote marks printed. Use three print statements for the six schedule lines, two lines each.

2. help.py. A help screen for a pretend tool called gradebook. It has a title, a usage line, a list of four options (-a add a score, -l list scores, -r print a report, -h show help), and two examples. One example uses the file path C:\Class\scores.txt. The other uses "Quiz 3" with the quote marks printed. Add a print line at the end that says Debug mode is on, then turn it off by making it a comment.

For schedule.py, ask Claude: "How did you print the quote marks around Bring your laptop without ending the text?"

For help.py, ask Claude: "Why does the file path need two backslashes in the code but only one shows up when it runs?" and "How did you turn off the debug line without deleting it?"

## Step 7. Make it yours

Have Claude write a fourth program that prints a track list for one of your releases. Use a border line, a title, and numbered tracks. Before you run it, say what you think the first three lines of output will be. Then run it and check.

## Step 8. Answer the questions

Open py01_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py01 printing and comments. Push.

## Turn in

All of these, pushed to your py01_outputAndComments folder:

1. welcome.py, schedule.py, help.py, and your own program
2. py01_Questions.md with your answers
