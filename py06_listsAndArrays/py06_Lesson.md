# py06 Lesson: Lists

You make three programs that store many values in a list. You learn how to get one item out of a list, how to loop through a whole list, and how to find the highest, lowest, and average yourself.

## What to know

1. A list holds many values in one variable, in order. It uses square brackets with commas between the items: scores = [88, 92, 75].
2. Each item has a position called an index. Indexes start at 0, not 1. scores[0] is the first item, 88. scores[2] is the third item, 75.
3. The last index is always one less than the number of items. Asking for an index that does not exist, like scores[3] in a list of 3 items, causes an IndexError.
4. len(scores) gives the number of items in the list.
5. An empty list is written []. scores.append(60) adds 60 to the end of the list. This is how a program fills a list from input.
6. scores[1] = 95 changes the second item to 95.
7. for score in scores: runs once for each item. Each time through, score holds the next item. Use this when you only need the values.
8. for i in range(len(scores)): runs once for each index. Each time through, i is the position, and scores[i] is the item. Use this when you need to know where an item is.
9. To find the highest value yourself: start with the first item as the highest so far. Loop through the list. Each time an item is bigger than the highest so far, it becomes the new highest so far. When the loop ends, you have the highest. The lowest works the same way with smaller.
10. The average is the total divided by the number of items. The total is a running total from py04.
11. To count items that match something, put a counter and an if inside the loop.
12. sorted(scores, reverse=True) makes a new list sorted from high to low. The original list stays in the order it was in. scores.sort() is different. It sorts the list itself and changes its order.
13. A function can take a whole list as a parameter.

## Step 1. Set up

1. Tell Claude: "Make a folder called py06_listsAndArrays in my repository folder."
2. On GitHub, open py06_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py06_Questions.md from my Downloads folder into my py06_listsAndArrays folder."

## Step 2. First program: Score Stats

Tell Claude:

"Write a Python program called scores.py and save it in my py06_listsAndArrays folder. Put a header comment at the top.

It asks How many scores. The answer must be 1 to 20, or it says Please enter 1 to 20 and asks again. Then it asks Score 1, Score 2, and so on, and stores the scores in a list.

Write three functions that each take the list: find_highest, find_lowest, and calculate_average. Use your own loop in each one. Do not use the built-in max, min, or sum.

Then print: all the scores in the order they were typed, the highest, the lowest, the average with 2 decimal places, how many scores are above the average, and the scores sorted high to low. Sorting must not change the order of the first line.

Use a main function. Give every function a comment. Put Input, Processing, and Output comments in main."

## Step 3. Run it

In the VS Code terminal, type: python scores.py

Type 5, then 88, 92, 75, 92, 60.

You should hear: Scores 88 92 75 92 60. Highest 92. Lowest 60. Average 81.40. Above average 3. Sorted high to low 92 92 88 75 60.

## Step 4. Explain

Tell Claude:

"Read me find_highest one line at a time. Then trace it for me with my 5 scores. Every time through the loop, tell me the score it is looking at and what the highest so far is."

Then ask Claude:

"How did the program fill the list from what I typed?"

"How did it count the scores above the average?"

"Why did the first line still show the scores in the order I typed them, after sorting?"

## Step 5. Break it on purpose

Tell Claude:

"In scores.py, change find_lowest so the lowest so far starts at 0 instead of the first score. Do not run it yet."

Before you run it, say what you think the lowest will be for the same 5 scores. Then run it. Ask Claude:

"Why did the lowest come out that way? Why is starting with the first item better than starting with 0?"

Tell Claude to fix it. Run it again to make sure it works.

## Step 6. Two more programs

For each program, first say the plan: what goes in the list, and what the program finds or counts by looping through it. Then tell Claude to write it. Run it. Then ask Claude to walk you through the code.

1. playlist.py. A list of 5 track lengths in seconds, typed into the program: 215, 340, 188, 262, 301. The program prints each one numbered, like Track 1: 215 seconds. Then it prints the total time in minutes and seconds, the longest track, and how many tracks are over 4 minutes, which is 240 seconds. You should hear a total of 21 minutes 46 seconds, a longest of 340 seconds, and 3 tracks over 4 minutes.

2. weather.py. A list of 7 high temperatures for a week, typed into the program: 51, 48, 55, 62, 58, 44, 50. The program finds the warmest day and the coldest day and prints them as day numbers, like Warmest: day 4 (62). It also prints the average. You should hear warmest day 4 at 62, coldest day 6 at 44, and an average of 52.57.

For playlist.py, ask Claude: "How did you turn the total seconds into minutes and seconds?"

For weather.py, ask Claude: "The list starts at index 0. How did you get day 4 for the warmest day?"

## Step 7. Make it yours

Have Claude write a program with a list of the names of your tracks. It prints them numbered starting at 1, then prints the first track and the last track using their indexes. Before you run it, say which index the last track is at. Then run it and check.

## Step 8. Answer the questions

Open py06_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py06 lists. Push.

## Turn in

All of these, pushed to your py06_listsAndArrays folder:

1. scores.py, playlist.py, weather.py, and your own program
2. py06_Questions.md with your answers
