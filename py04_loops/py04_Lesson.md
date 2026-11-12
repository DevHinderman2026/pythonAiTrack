# py04 Lesson: Loops

You make three programs that repeat things. You learn the two kinds of loops in Python, how to count and keep a total inside a loop, and how to let the user play again.

## What to know

1. A loop runs the same lines more than once. The lines inside the loop are indented under it, the same as an if.
2. A while loop repeats as long as its comparison is True. Python checks the comparison before each time through. When it is False, the loop ends and the program goes on to the next line after the loop.
3. If the comparison never becomes False, the loop never ends. This is called an infinite loop. Press Control plus C in the terminal to stop it.
4. A counter is a variable that starts at 0 and goes up by 1 each time something happens, like count = count + 1. A running total starts at 0 and adds a value each time, like total = total + amount. Both have to be set to 0 before the loop starts.
5. A loop that asks again: ask once before the loop. While the answer is bad, print a message and ask again. When the loop ends, the answer is good.
6. A for loop runs once for each value in a list of values. range makes that list of numbers. range(1, 6) gives 1, 2, 3, 4, 5. It stops before the second number. So to count from 1 to some number n, use range(1, n + 1).
7. In for i in range(1, 6), the variable i holds the current number. It is 1 the first time, 2 the second time, and so on.
8. continue skips the rest of the lines in the loop for this time through and goes back to the top of the loop.
9. import random at the top of the program lets you use random numbers. random.randint(1, 100) picks a whole number from 1 to 100. Both 1 and 100 can be picked.
10. A loop can be inside another loop. In a guessing game, the outside loop is play again, and the inside loop is keep guessing.

## Step 1. Set up

1. Tell Claude: "Make a folder called py04_loops in my repository folder."
2. On GitHub, open py04_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py04_Questions.md from my Downloads folder into my py04_loops folder."

## Step 2. First program: Number Guessing Game

Tell Claude:

"Write a Python program called guess.py and save it in my py04_loops folder. Put a header comment at the top.

The computer picks a secret whole number from 1 to 100 and prints I'm thinking of a number from 1 to 100. It keeps asking Your guess until the player gets it. After each wrong guess it prints Too low or Too high. A guess below 1 or above 100 prints Please guess between 1 and 100, and does not count as a guess.

When the player gets it, print You got it in, the number, and guesses. Use guess instead of guesses for 1. Then use a for loop to print Guess chart, followed by one star for each guess.

Then ask Play again, y or n. y or Y starts a new game with a new secret number. Anything else ends it and prints Thanks for playing, and how many games were played.

Use an outside while loop for play again and an inside while loop for guessing. Put Input, Processing, and Output comments above each part."

## Step 3. Run it

The secret number is random, so it is hard to test. Tell Claude:

"In guess.py, make the secret number always 42 for now, and put a comment saying to change it back."

In the VS Code terminal, type: python guess.py

Guess 50, then 150, then 25, then 42. You should hear Too high, then the between 1 and 100 message, then Too low, then You got it in 3 guesses, and a chart of 3 stars. The 150 does not count. Play one more game and guess 42 first. You should hear 1 guess. Then type n.

Tell Claude to put the random number back. Play one real game.

## Step 4. Explain

Tell Claude:

"Read me guess.py one part at a time. For each loop, tell me what it repeats and what makes it stop."

Then ask Claude:

"Which variables are counters, and where do they get set back to 0?"

"How does continue make the 150 guess not count?"

"How does the for loop make the guess chart?"

## Step 5. Break it on purpose

Tell Claude:

"In guess.py, change the guess chart loop so the range starts at 1 and stops at the number of guesses, with no plus 1. Make the secret number 42 again. Do not run it yet."

Before you run it, say how many stars you think 3 guesses will print. Then run it and guess 50, 25, 42. Ask Claude:

"Why did the chart print that many stars?"

Tell Claude to fix the chart loop and put the random number back. Run it again to make sure it works.

## Step 6. Two more programs

For each program, first say the plan: what repeats, what makes it stop, and what it keeps track of. Then tell Claude to write it. Run it with the test answers. Then ask Claude to walk you through the code.

1. times.py. A times table builder. It asks for a number from 1 to 12 and how many rows from 1 to 20. If an answer is out of range, it says so and asks again. It prints the times table with a for loop, one line per row, like 7 x 1 = 7. While it prints, it keeps a running total of the answers and counts how many answers are even. Then it prints the sum and the even count, and asks Make another table. At the end it prints how many tables were made. Test it with 7 and 5 rows. You should hear 7 through 35, a sum of 105, and 2 even answers of 5.

2. savings.py. A savings goal tracker. It asks for a name and a savings goal. Then it keeps asking for a deposit for Week 1, Week 2, and so on, while the amount saved is less than the goal. A deposit of 0 or less prints Deposits must be more than 0 dollars and asks again for the same week. After each good deposit it prints the amount saved so far and how much is left to go. At the end it prints how many weeks it took, the total saved, the biggest deposit, the average deposit, and how far over the goal it went. Test it with Jordan, a goal of 100, and deposits of 25, 0, 30, 20, 40. You should hear 4 weeks, $115.00 saved, $40.00 biggest, and $28.75 average.

For times.py, ask Claude: "Why does the running total get set back to 0 at the start of each table and not at the top of the program?"

For savings.py, ask Claude: "How does the program keep track of the biggest deposit?"

## Step 7. Make it yours

Have Claude write a program that asks how many tracks are on a release, then asks for the length of each track in minutes using a for loop. It prints the total length and the longest track. Before you run it, pick your answers and figure out the total and the longest yourself. Then run it and check.

## Step 8. Answer the questions

Open py04_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py04 loops. Push.

## Turn in

All of these, pushed to your py04_loops folder:

1. guess.py, times.py, savings.py, and your own program
2. py04_Questions.md with your answers
