# py02 Lesson: Variables, Input, and Math

You make three programs that ask the user questions, do math with the answers, and print the results. You learn how a program stores values, how it reads what the user types, and how it shows money with two decimal places.

## What to know

1. A variable is a name that holds a value. The line `name = "Jordan"` stores the text Jordan in a variable called name. The equal sign means store this value. It does not mean is equal to.
2. When a variable gets a new value, the old value is gone.
3. Python has different types of values. A string is text, like "Pretzel". An int is a whole number, like 3. A float is a number with a decimal point, like 2.75.
4. input shows a prompt, waits for the user to type something and press Enter, and gives back what they typed. What input gives back is always a string, even if the user typed a number.
5. int() turns text into a whole number. float() turns text into a decimal number. You need them before you can do math with what the user typed. If you use plus on two strings, Python joins them instead of adding, so "5" + "7" gives "57".
6. Math in Python: plus, minus, star for times, slash for divide. Slash always gives a decimal answer. Two slashes divides and drops the leftover part, so 30 // 8 is 3. The percent sign gives the leftover part, so 30 % 8 is 6.
7. A named constant is a variable written in capital letters, like TAX_RATE = 0.07. The capital letters tell the reader it is not supposed to change. If the tax rate changes, you change it in one place at the top of the program.
8. An f-string puts variables inside text. It starts with the letter f before the quote mark, and the variable goes in curly braces: f"Total: {total}". Adding :.2f after the variable name shows it with exactly 2 decimal places, so money looks like $8.83.
9. print can show more than one value. Separate them with commas, and Python puts one space between them. print("Score", 95) prints Score 95.
10. Most programs follow the same order. Input: get the values. Processing: do the math. Output: show the results.

## Step 1. Set up

1. Tell Claude: "Make a folder called py02_variablesAndInput in my repository folder."
2. On GitHub, open py02_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py02_Questions.md from my Downloads folder into my py02_variablesAndInput folder."

## Step 2. First program: Snack Bar Order

Tell Claude:

"Write a Python program called snack.py and save it in my py02_variablesAndInput folder. Put a header comment at the top. Store the tax rate in a constant called TAX_RATE set to 0.07.

The program asks four questions with these prompts: Customer name, Item, Price, and Quantity. The price is a decimal. The quantity is a whole number.

Then it figures out the subtotal, which is price times quantity, the tax, which is subtotal times the tax rate, and the total, which is subtotal plus tax.

Then it prints a blank line and a receipt: a title line that says Receipt for and the customer's name, then lines for the item, the quantity, the subtotal, the tax, and the total. Show money with a dollar sign and 2 decimal places. Put Input, Processing, and Output comments above each part."

## Step 3. Run it

In the VS Code terminal, type: python snack.py

Type these answers: Jordan, Pretzel, 2.75, 3.

You should hear a receipt with a subtotal of $8.25, tax of $0.58, and a total of $8.83.

## Step 4. Explain

Tell Claude:

"Read me snack.py one part at a time: the input part, the processing part, and the output part. For each part, tell me what it does and which variables it makes."

Then ask Claude:

"Why does the price need float and the quantity need int?"

"What does :.2f do in the receipt lines?"

"Why is TAX_RATE in capital letters? What would I change if the tax went up to 8 percent?"

## Step 5. Break it on purpose

Tell Claude:

"In snack.py, take out the float around the price input. Do not run it yet."

Before you run it, say what you think will happen. Then run it with the same answers. Ask Claude:

"What does this error mean? Why did taking out float cause it?"

Tell Claude to put float back. Run it again to make sure it works.

## Step 6. Two more programs

For each program, first say the plan: what the program asks, what math it does, and what it prints. Then tell Claude to write it. Run it with the test answers. Then ask Claude to walk you through the code.

1. pizza.py. A pizza party planner. Constants: 8 slices per pizza, $12.99 per pizza, $2.25 per extra slice. It asks for the host's name, the number of people, and slices per person. It figures out total slices, whole pizzas using two slashes, extra slices using the percent sign, the total cost, and the cost per person. It prints a title like Pizza Plan for Jordan's Party and one line for each result. Test it with Jordan, 10 people, 3 slices each. You should hear 30 slices, 3 whole pizzas, 6 extra slices, total cost $52.47, cost per person $5.25.

2. trip.py. A road trip calculator. One constant: average speed of 55 miles per hour. It asks for the destination, the trip distance in miles, the car's miles per gallon, the gas price, and how many people split the cost. It figures out gallons of gas, gas cost, cost per person, and driving time in hours and minutes. Test it with Columbus, 150, 30, 3.20, 2. You should hear 5.0 gallons, $16.00 gas cost, $8.00 per person, and 2 hours 43 minutes.

For pizza.py, ask Claude: "Walk me through how 30 slices turns into 3 pizzas and 6 extra slices."

For trip.py, ask Claude: "How did the program turn the driving time into hours and minutes?"

## Step 7. Make it yours

Have Claude write a program that asks how many tracks are on a release and how many minutes long each track is on average. It prints the total length in hours and minutes. Before you run it, pick your answers and figure out the total yourself. Then run it and check.

## Step 8. Answer the questions

Open py02_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py02 variables and input. Push.

## Turn in

All of these, pushed to your py02_variablesAndInput folder:

1. snack.py, pizza.py, trip.py, and your own program
2. py02_Questions.md with your answers
