# py10 Lesson: Handling Errors

You make three programs that do not crash when the user types something wrong. You learn how to read an error message, how to catch an error with try and except, and how to write input functions you can use in any program.

## What to know

1. An exception is an error that happens while the program is running. Typing two when the program wants a number causes one. If the program does not handle it, the program stops and prints an error message called a traceback.
2. Read a traceback from the bottom up. The last line says the type of error and what went wrong. The lines above it give the line number and the line of code where it happened.
3. Common types of errors: ValueError is a value that cannot be used, like int("two"). ZeroDivisionError is dividing by zero. FileNotFoundError is a file that is not there. IndexError is an index that does not exist. TypeError is using the wrong type, like doing math with None.
4. try and except catch errors. Python runs the lines under try. If one of them causes an error, Python jumps to the lines under except instead of crashing. If nothing goes wrong, the except lines are skipped.
5. except ValueError: catches only ValueErrors. Name the error you expect. A plain except with no error name catches everything, including mistakes in your own code, which makes them hard to find.
6. else after a try runs only if there was no error. finally runs every time, error or not.
7. int("2.5") is a ValueError too. So int() turns away decimals as well as letters.
8. The line that might fail has to be inside the try. If int(input()) is above the try, the error happens before the try starts, and the program still crashes.
9. The ask until valid loop: while True: starts a loop that only ends when something stops it. Inside, try to turn the answer into a number. If it works and is in range, return it, which ends the function and the loop. If not, print a message, and the loop asks again.
10. A reusable input function is written once and used everywhere. get_int(prompt, low, high) gets a whole number in a range. get_text(prompt) gets an answer that is not blank. get_yes_no(prompt) gets y or n and returns True or False.
11. A blank answer is the user just pressing Enter. An answer of only spaces should count as blank too, so strip it first, then check if it equals "".
12. To test error handling, try everything a user might type wrong: letters, decimals, a blank, a number that is too small or too big, and the numbers right at the edges.

## Step 1. Set up

1. Tell Claude: "Make a folder called py10_errorHandling in my repository folder."
2. On GitHub, open py10_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py10_Questions.md from my Downloads folder into my py10_errorHandling folder."

## Step 2. See a crash first

Tell Claude:

"Write a two line program called crash.py in my py10_errorHandling folder. It asks How many tickets, turns the answer into an int, and prints it."

Run it with python crash.py and type two. Listen to the traceback. Ask Claude:

"Read me this traceback from the bottom up. What type of error is it, and which line caused it?"

## Step 3. First program: Ticket Order

Tell Claude:

"Write a Python program called tickets.py and save it in my py10_errorHandling folder. Put a header comment at the top.

Write these reusable functions:
get_text keeps asking until the answer is not blank. On a blank it prints This cannot be blank.
get_int takes a prompt, a low number, and a high number. It keeps asking until the answer is a whole number in that range. Otherwise it prints Please enter a whole number from, the low number, to, the high number. It must turn away letters, decimals, blanks, and numbers out of range without crashing.
get_yes_no returns True for y or Y and False for n or N. Anything else prints Please enter y or n and asks again.

The program asks for the name. Then it shows the ticket types: 1 Student $5.00, 2 Adult $8.50, 3 Senior $6.25. It asks the ticket type 1 to 3 and the quantity 1 to 10, adds that to the order, and asks Another order. It repeats until the answer is no. Then it prints the total tickets and total cost.

Then it saves the order to orders.txt, one line per order, like Jordan,Adult,3,25.50. Put the saving inside try and except. On success print Order saved to orders.txt. If saving fails, print Error: could not save orders.txt.

Store the ticket names and prices in two parallel lists. Use a main function. Give every function a comment. Put a comment on each try and except saying what error it catches."

## Step 4. Run it

In the VS Code terminal, type: python tickets.py

Type these answers, one at a time:

1. Press Enter with nothing typed. You should hear This cannot be blank.
2. Jordan.
3. Ticket type: two. Then 2.
4. Quantity: 2.5. Then 3.
5. Another order: maybe. Then y.
6. Ticket type 1. Quantity 2. Another order: n.

You should hear Total tickets 5 and Total cost $35.50, then Order saved. Tell Claude: "Read me orders.txt." You should hear two lines, one for the Adult tickets and one for the Student tickets.

## Step 5. Explain

Tell Claude:

"Read me get_int one line at a time. Then trace it for me when I type two, then 2.5, then 9, then 2, with a range of 1 to 3."

Then ask Claude:

"How does while True ever stop in get_int?"

"How does get_text know that a few spaces count as blank?"

"What error does the try around the saving catch, and what would cause it?"

## Step 6. Break it on purpose

Tell Claude:

"In tickets.py, move the line in get_int that turns the answer into an int so it is above the try instead of inside it. Do not run it yet."

Before you run it, say what you think will happen when you type two for the ticket type. Then run it. Ask Claude:

"Why did it crash even though there is a try and except?"

Tell Claude to put the line back inside the try. Run it again with two to make sure it works.

## Step 7. Two more programs

For each program, first say the plan: what could go wrong, and what the program should do instead of crashing. Then tell Claude to write it. Run it with the test answers. Then ask Claude to walk you through the code.

1. guess2.py. Tell Claude: "Copy guess.py from my py04_loops folder into my py10_errorHandling folder as guess2.py. Copy get_int from tickets.py into it, and use get_int for the guess, with a range of 1 to 100. Take out the old range check." Run it and type letters for a guess. It should ask again instead of crashing.

2. average.py. It asks Enter a number, or press Enter to finish, over and over. Letters print That is not a number and do not count. A blank answer ends the loop. Then it prints the average with 2 decimal places. If no numbers were entered, dividing by zero would cause a ZeroDivisionError. Catch it and print No numbers entered. Test it with 10, abc, 20, then a blank. You should hear an average of 15.00. Run it again and only press Enter. You should hear No numbers entered.

For guess2.py, ask Claude: "Why could I delete the old range check?"

For average.py, ask Claude: "Which error does each except catch, and what causes each one?"

## Step 8. Make it yours

Have Claude write a program that asks for a track's tempo in beats per minute. It uses get_int with a range of 40 to 220. Then it asks whether the track is finished, using get_yes_no, and prints a short summary. Before you run it, make a list of three wrong answers to try. Then run it and try them.

## Step 9. Answer the questions

Open py10_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 10. Push

Commit with the summary py10 error handling. Push.

## Turn in

All of these, pushed to your py10_errorHandling folder:

1. crash.py, tickets.py, orders.txt, guess2.py, average.py, and your own program
2. py10_Questions.md with your answers
