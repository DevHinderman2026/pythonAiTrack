# py02 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py02_variablesAndInput folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. What is a variable? What does the equal sign do in the line `name = "Jordan"`?

Answer: A variable in Python is like a container that can hold an item. The equal sign sets the value for the variable on the left, whatever is on the right, for example, name = "Jordan".

### 2. What is the difference between a string, an int, and a float? Give one example of each.

Answer: A string is text with quotes. This is so that Python can distinguish it from a variable name, for example, "cat". An int, or integer, is a whole number with no decimal, for example, 5. A float is a number with a decimal, for example, 7.00. This is especially useful in the context of money, like $7.50.

### 3. What type of value does input always give back? Why does that matter?

Answer: Input will always give back text, so if you input a number, the program can silently make a mistake.

### 4. What is a named constant? Why is it better than typing the number everywhere it is used?

Answer: A constant is a name with a number that does not change in the program. For example, a tax rate in a snack program. A constant is better than typing numbers throughout the whole program. If you need to make a change, you change the constant only. It's better to use constants rather than relying on your own memory of which number is which, and this prevents errors.

### 5. What is the difference between one slash and two slashes? What does the percent sign give you?

Answer: If there is one /, then you will get a number with decimals. If there are two slashes, you get a number which is whole and the remainder is dropped. If you use the percent sign, you would get the remainder only.

## Part 2. Your programs

### 6. In snack.py, what are the input, processing, and output parts? Say what each one does.

Answer: Input: First, an input is a prompt to the user. The inputs are stored in variables. For example, enter the name of who is purchasing the item, what the price of the item is, and the quantity. All of these get stored in their own container. Processing: The processing part of the program will take all of the inputs you give and calculate. The calculations are subtotal, tax, and total. Output: The print statements are printing what the item is, how much the quantity, the subtotal, the tax, and the total all together.

### 7. In Step 5 you took out float. What happened when you ran it, and why?

Answer: A name error took place on line 25. Everything ran up to that point. A name for a variable was not spelled correctly.

### 8. In pizza.py, explain how the program got 3 whole pizzas and 6 extra slices from 30 slices.

Answer: The number of pizzas that is whole comes from the 2 slashes. The percent sign calculates the number of slices left over to determine the extra slice count. The left over is slices only.

## Part 3. Read the code

### 9. What does this program print? Write the output exactly.

```python
# Processing
price = 4
quantity = 3
total = price * quantity
price = 10
# Output
print(f"Total: ${total:.2f}")
```

Answer: NOTE FOR MR. MCMASTER: I could not answer this question on my own. I tried several times and got it wrong, and Claude walked me through the lines one at a time. I am still having trouble understanding it, so I would like help with it. - Russell

### 10. The user types 5 and then 7. What does this program print, and why?

```python
# Input
first = input("First number: ")
second = input("Second number: ")
# Output
print(first + second)
```

Answer: It prints 57. First and second are put together. Inputs use text unless you convert.
