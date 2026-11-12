# py05 Lesson: Functions

You make three programs that are split into functions. A function is a small named piece of a program that does one job. You learn how to send values into a function, how to get a value back out, and how to follow a program as it jumps from function to function.

## What to know

1. A function is a named group of lines that does one job. def starts a function. def calculate_tax(subtotal): makes a function called calculate_tax. The lines inside are indented under it.
2. Defining a function does not run it. Calling it runs it. You call a function by writing its name with parentheses, like calculate_tax(8.25).
3. A parameter is a name in the parentheses of the def line. It receives a value. An argument is the value you put in the parentheses when you call the function. The first argument goes into the first parameter, the second into the second, and so on.
4. return sends a value back to the line that called the function. That line can store it in a variable, like tax = calculate_tax(subtotal). When return runs, the function is done.
5. print and return are different. print shows a value on the screen. return hands a value back so the program can use it. A function with no return gives back None, which means nothing. You cannot do math with None.
6. Every function gets a comment that says its purpose, its parameters, and what it returns. The comment can be lines starting with a pound sign, or text inside three quote marks on the line right under def. The three quote marks kind is called a docstring.
7. A variable made inside a function only exists inside that function. This is called a local variable. Other functions cannot see it. Values go into a function through parameters and come out through return.
8. A function can call other functions.
9. Most programs have a function called main that holds the main steps of the program, in order. The last two lines of the file start it: if __name__ == "__main__": and then main(). Reading main is the fastest way to find out what a program does.
10. When a function is called, Python jumps to that function, runs its lines, and then comes back to the line that called it. Following those jumps is called tracing a program.

## Step 1. Set up

1. Tell Claude: "Make a folder called py05_functions in my repository folder."
2. On GitHub, open py05_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py05_Questions.md from my Downloads folder into my py05_functions folder."

## Step 2. First program: Snack Bar with Functions

Tell Claude:

"Write a Python program called snack2.py and save it in my py05_functions folder. It is a snack bar order like the one in py02, but an order can have several items. Put a header comment at the top and TAX_RATE = 0.07 as a constant.

It asks for the customer name. Then it asks for an item, price, and quantity, and then Add another item, y or n, and keeps going until the answer is n.

Write these functions:
calculate_subtotal takes price and quantity and returns price times quantity.
calculate_tax takes a subtotal and returns subtotal times TAX_RATE.
format_money takes an amount and returns it as text with a dollar sign and 2 decimal places.
print_receipt takes the name, the item count, and the subtotal. It prints the receipt with the number of items, the subtotal, the tax, and the total. It calls calculate_tax and format_money.
main asks the questions, keeps the running subtotal and item count, and calls print_receipt.

Give every function a comment with its purpose, parameters, and return value. End the file with the main guard. Put Input, Processing, and Output comments in main."

## Step 3. Run it

In the VS Code terminal, type: python snack2.py

Type Jordan. Then Pretzel, 2.75, 3, y. Then Lemonade, 1.50, 2, n.

You should hear 5 items ordered, subtotal $11.25, tax $0.79, total $12.04.

## Step 4. Explain

Tell Claude:

"Read me the main function in snack2.py first, one line at a time. Then read me each of the other functions and tell me which line in main calls it."

Then ask Claude:

"Trace the program for me when I order the pretzel. Every time it jumps to a function, tell me what values go in and what comes back."

"Which functions return a value and which ones only print? Why is it set up that way?"

"Could print_receipt use the variable order_subtotal from main directly? Why or why not?"

## Step 5. Break it on purpose

Tell Claude:

"In snack2.py, change calculate_tax so it prints the tax instead of returning it. Do not run it yet."

Before you run it, say what you think will happen. Then run it with the same answers. Ask Claude:

"What does this error mean? Why did changing return to print cause it?"

Tell Claude to put return back. Run it again to make sure it works.

## Step 6. Two more programs

For each program, first say the plan: what functions it needs, what each one takes in, and what each one gives back. Then tell Claude to write it. Run it with the test answers. Then ask Claude to walk you through the code.

1. temperature.py. A temperature converter. Functions: f_to_c returns the Celsius temperature for a Fahrenheit one. c_to_f does the opposite. describe takes a Fahrenheit temperature and returns Freezing for 32 or below, Cold below 50, Mild below 70, Warm below 85, or Hot. print_result prints the two result lines. main asks Convert from F or C, then the temperature, prints the result, and asks Convert another. At the end it prints how many conversions were done. Show temperatures with 1 decimal place. Test it with F and 72. You should hear 72.0 F = 22.2 C and That feels Warm. Then try C and minus 5. You should hear 23.0 F and Freezing.

2. gradereport.py. A class grade report. Constant: passing average of 60. Functions: get_average takes three scores and returns their average. letter_grade takes an average and returns A, B, C, D, or F. is_passing takes an average and returns True or False. print_report_line prints one line like Avery: average 91.7, grade A, PASS. main asks how many students, then each name and three scores, then prints a class summary with the class average, how many passed, and the top student. Test it with 2 students: Avery with 92, 88, 95, and Sam with 55, 62, 48. You should hear Avery 91.7 A PASS, Sam 55.0 F FAIL, and Avery as the top student.

For temperature.py, ask Claude: "When I convert from C, why does describe get the Fahrenheit number?"

For gradereport.py, ask Claude: "How does is_passing give back True or False in one line?"

## Step 7. Make it yours

Have Claude write a program with a function called seconds_to_time. It takes a track length in seconds and returns text like 3:25. main asks for three track lengths in seconds and prints each one using the function. Before you run it, pick three lengths and figure out what each one should print. Then run it and check.

## Step 8. Answer the questions

Open py05_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py05 functions. Push.

## Turn in

All of these, pushed to your py05_functions folder:

1. snack2.py, temperature.py, gradereport.py, and your own program
2. py05_Questions.md with your answers
