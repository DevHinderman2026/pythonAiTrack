# py08 Lesson: Tables of Data

You make three programs that store data in rows and columns, like a table. You learn how to store a table in a list of lists, how to loop through every row and column, how to keep two lists lined up, and how to store pairs of values in a dictionary.

## What to know

1. A list can hold other lists. A list of lists works like a table. Each inner list is one row. scores = [[80, 90, 70], [95, 85, 88]] is a table with 2 rows and 3 columns.
2. scores[row][column] gets one value. Both start at 0. scores[1][0] is row 1, column 0, which is 95.
3. A nested loop is a loop inside a loop. To go through a table, the outside loop goes through the rows. The inside loop goes through the columns in that row. The inside loop runs all the way through every time the outside loop goes once.
4. A row total adds up the values across one row. A column average adds up the values down one column, in every row, then divides by the number of rows.
5. Parallel lists are two lists where the same index means the same thing. If names[1] is Taylor, then scores[1] is Taylor's row of scores. If you sort one list, you have to move the other list the same way, or the names and scores get mixed up.
6. A dictionary stores pairs. Each pair has a key and a value. plays = {"Intro": 120, "Echoes": 300} has two keys. plays["Echoes"] gives 300. plays["Outro"] = 50 adds a new pair. for name in plays: loops through the keys. len(plays) gives the number of pairs. Setting a key that is already there replaces its value. Each key can only be in a dictionary once.
7. Bubble sort is one way to sort by hand. It walks through the list comparing each item with the one next to it. If they are in the wrong order, it swaps them. It keeps walking through the list until it makes a pass with no swaps.
8. To line up columns, an f-string can pad a value to a set width. f"{name:<10}" prints the name and fills spaces after it until it is 10 characters wide. The less than sign means line it up on the left.
9. To find the best value in a whole table, start with row 0, column 0 as the best so far. Loop through every row and column. Each time you find a bigger value, remember the value and which row and column it was in.

## Step 1. Set up

1. Tell Claude: "Make a folder called py08_nestedData in my repository folder."
2. On GitHub, open py08_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py08_Questions.md from my Downloads folder into my py08_nestedData folder."

## Step 2. First program: Team Scoreboard

Tell Claude:

"Write a Python program called scoreboard.py and save it in my py08_nestedData folder. Put a header comment at the top and a constant NUM_ROUNDS = 3.

It asks How many players, 1 to 6, and asks again if it is out of range. Then it asks each player's name. Then for each player it asks a score for each of the 3 rounds, like Jordan, round 1 score. Scores must be 0 to 100, or it says Score must be 0 to 100 and asks that same round again.

Store the names in a list and the scores in a list of lists, one row per player.

Sort the players by total score, highest first, with a bubble sort that moves the names and the score rows together. Print a leaderboard table with columns for Name, R1, R2, R3, Total, and Average with 2 decimal places, with a line of dashes under the header. Line up the columns.

Then print the winner with their total, the best single round with the player, round number, and score, and the round with the highest average across all players.

Use functions for getting the scores, figuring out a player's total, sorting, printing the table, and the analysis. Use a main function. Give every function a comment. Put Input, Processing, and Output comments in main."

## Step 3. Run it

In the VS Code terminal, type: python scoreboard.py

Type 3 players: Jordan, Taylor, Sam. Then these scores:

Jordan: 80, 90, 70.
Taylor: 95, 85, 88.
Sam: 60, 75, 105, then 100 when it asks again.

You should hear the table in this order: Taylor with 268, Jordan with 240, Sam with 235. Then Winner Taylor, best single round Sam round 3 with 100, and highest scoring round Round 3 with an average of 86.00.

## Step 4. Explain

Tell Claude:

"Read me the table of scores as a grid, one row at a time, with the player's name. Then read me the function that prints the table, and tell me what the outside loop and the inside loop each do."

Then ask Claude:

"How does the program find the average for one round? Which loop goes across and which goes down?"

"Walk me through one pass of the bubble sort with my three players."

"How does the program remember which player and which round had the best single score?"

## Step 5. Break it on purpose

Tell Claude:

"In scoreboard.py, change the sort so it swaps the score rows but does not swap the names. Do not run it yet."

Before you run it, say what you think the table will look like. Then run it with the same answers. Ask Claude:

"Why are the names and scores mixed up now? Why do parallel lists have to move together?"

Tell Claude to fix the sort. Run it again to make sure it works.

## Step 6. Two more programs

For each program, first say the plan: how the data is stored, and what the program loops through to find each answer. Then tell Claude to write it. Run it. Then ask Claude to walk you through the code.

1. reading.py. A reading log typed into the program. Names: Avery, Blake, Casey. A list of lists of pages read in 4 weeks: Avery 30, 45, 20, 50. Blake 25, 10, 40, 35. Casey 60, 25, 15, 20. The program prints each student's total, the average for each week with 2 decimal places, which week had the most reading, and the highest single week with the student and week number. You should hear totals of 145, 110, and 120. Week averages of 38.33, 26.67, 25.00, and 35.00. Week 1 had the most reading. The highest single week was Casey in week 1 with 60.

2. plays.py. A dictionary of tracks and how many times each one was played, typed into the program: Intro 120, Night Drive 340, Echoes 275, Outro 90. The program prints every track and its plays, the total plays, and the most played track. Then it asks for a new track name and its plays, adds it to the dictionary, and prints the list again. You should hear a total of 825 and Night Drive as the most played.

For reading.py, ask Claude: "How did you get the week number from the column index?"

For plays.py, ask Claude: "What is the key and what is the value in this dictionary? How did you add the new track?"

## Step 7. Make it yours

Have Claude write a program with a list of lists for 3 of your tracks and how many plays each one got on Monday, Tuesday, and Wednesday. It prints a lined-up table with a total for each track. Before you run it, pick the numbers and figure out one track's total yourself. Then run it and check.

## Step 8. Answer the questions

Open py08_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py08 tables of data. Push.

## Turn in

All of these, pushed to your py08_nestedData folder:

1. scoreboard.py, reading.py, plays.py, and your own program
2. py08_Questions.md with your answers
