# py03 Lesson: Making Decisions with If

You make three programs that make decisions. Each one checks the user's answers and does different things depending on what they typed.

## What to know

1. A comparison asks a yes or no question and gives back True or False. The comparisons are: == for equal, != for not equal, < for less than, > for greater than, <= for less than or equal, and >= for greater than or equal.
2. One equal sign stores a value in a variable. Two equal signs compare two values. Mixing them up is a common mistake.
3. An if statement runs some lines only when a comparison is True. The if line ends with a colon. The lines that belong to the if are indented 4 spaces under it. The indent is how Python knows which lines are inside the if.
4. else goes after an if. Its lines run when the comparison is False. With if and else, exactly one of the two parts runs.
5. elif means else if. It lets a program check several choices in order, from the top down. The first one that is True runs, and Python skips the rest. That is why order matters: a grade checker has to check for 90 before it checks for 80.
6. and is True only when both sides are True. or is True when at least one side is True. not flips True to False and False to True.
7. Two separate if statements both get checked. An if with elif stops at the first True one. Use separate ifs when more than one thing can apply at the same time.
8. Text comparisons are exact. "Tuesday" == "tuesday" is False because of the capital letter. .lower() turns text into all lowercase letters first, so the check works no matter how the user typed it.
9. Test the edges. If 60 is passing, test 59, 60, and 61. Most mistakes happen right at the line between two choices.

## Step 1. Set up

1. Tell Claude: "Make a folder called py03_ifStatements in my repository folder."
2. On GitHub, open py03_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py03_Questions.md from my Downloads folder into my py03_ifStatements folder."

## Step 2. First program: Grade Checker

Tell Claude:

"Write a Python program called grades.py and save it in my py03_ifStatements folder. Put a header comment at the top.

It asks for a student name and a score from 0 to 100, a whole number.

If the score is below 0 or above 100, it prints Error: score must be 0 to 100, and nothing else. Use or for this check.

Otherwise it prints the name, then got a, then the letter grade. 90 to 100 is A, 80 to 89 is B, 70 to 79 is C, 60 to 69 is D, below 60 is F. Use an instead of a before A and F, like got an A.

Then it prints that the student passed for 60 or higher, or did not pass. If the score is exactly 100, it also prints Perfect score! as the last line.

Use an if, elif, else chain for the letter. Put Input, Processing, and Output comments above each part."

## Step 3. Run it

In the VS Code terminal, type: python grades.py

Run it four times:

1. Taylor, 87. You should hear Taylor got a B, Taylor passed.
2. Sam, 105. You should hear the error message only.
3. Riley, 100. You should hear got an A, passed, and Perfect score.
4. Max, 42. You should hear got an F and did not pass.

Then test the edges: 59, 60, 89, 90.

## Step 4. Explain

Tell Claude:

"Read me grades.py one part at a time. For each if, elif, and else, tell me the question it asks and what happens when the answer is yes."

Then ask Claude:

"Why does the range check use or instead of and?"

"How does the program decide between a and an?"

"Which lines are inside the else of the range check? How does Python know?"

## Step 5. Break it on purpose

Tell Claude:

"In grades.py, move the check for D to the top of the letter grade chain, so it checks for 60 or higher first. Do not run it yet."

Before you run it, say what letter you think a score of 87 will get. Then run it with 87. Ask Claude:

"Why did 87 get that letter? Why does the order of the elif checks matter?"

Tell Claude to put the order back. Run it again with 87 to make sure it works.

## Step 6. Two more programs

For each program, first say the plan: what it asks, what decisions it makes, and what it prints. Then tell Claude to write it. Run it with the test answers. Then ask Claude to walk you through the code.

1. movie.py. A movie ticket price. Constants: child $7.00, adult $11.00, senior $8.00, Tuesday discount $3.00, 3D charge $2.50. It asks for a name, age, day of the week, and whether the movie is 3D, y or n. If the age is below 0 or above 120, print an error. Under 13 is a child ticket, 65 or older is senior, everyone else is adult. On Tuesday, take off the discount. It must work for Tuesday, tuesday, or TUESDAY. If 3D, add the charge. Print the ticket type, base price, the Tuesday deal line only if it applies, the 3D line only if it applies, and the total. Test it with Mia, 9, Tuesday, y. You should hear Child, $7.00, a $3.00 Tuesday deal, a $2.50 3D charge, and a total of $6.50.

2. shipping.py. A shipping calculator. It asks for the order total, the weight in pounds, the zone 1, 2, or 3, and rush delivery y or n. Zone 1 costs 50 cents a pound and takes 2 days. Zone 2 costs 75 cents a pound and takes 4 days. Zone 3 costs $1.25 a pound and takes 6 days. Shipping is never less than $4.00. Orders of $50 or more ship free if they are not rush. Rush adds $10 and takes 1 day, or 2 days for zone 3. Print the order total, shipping, grand total, and how many days. Print FREE when shipping is free. Test it with 64.50, 3, 1, n. You should hear shipping FREE, grand total $64.50, 2 days.

For movie.py, ask Claude: "Why are the Tuesday check and the 3D check two separate ifs instead of an elif?"

For shipping.py, ask Claude: "Walk me through the free shipping rule. Why does it need and and not?"

## Step 7. Make it yours

Have Claude write a program that asks how many plays a track has, and prints a label: under 100 is New, 100 to 999 is Growing, 1000 or more is Popular. Before you run it, pick three numbers that test the edges, like 99, 100, and 1000. Say what label each one should get. Then run it and check.

## Step 8. Answer the questions

Open py03_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py03 if statements. Push.

## Turn in

All of these, pushed to your py03_ifStatements folder:

1. grades.py, movie.py, shipping.py, and your own program
2. py03_Questions.md with your answers
