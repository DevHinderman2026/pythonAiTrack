# py01 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py01_outputAndComments folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. In what order does Python run the lines in a program?

Answer:

Python will run the program from top to bottom left to right.

### 2. What does print do?

Answer:

Print prints a statement on screen. For example, hello. However, the statement needs to be in quotes.

### 3. What is a comment? What does Python do with a comment when the program runs?

Answer:

The commented line starts with a number sign. Python skips that line. This is useful for when your writing program notes.

### 4. What goes in the header comment at the top of a program? Why is it useful to someone reading your code?

Answer:

In the header of a program the following info is presented. 1. Your Name: 2. Date 3. program name 4. summary of program. This is very useful for developers looking at your code for the first time.

## Part 2. Your programs

### 5. In welcome.py, how did one print statement make two lines of output?

Answer:

Back slash n creates a new line within the print statement.

### 6. In schedule.py, how did the program print quote marks around Bring your laptop?

Answer:

The back slash with quote would print the quote mark instead of ending the current string.

### 7. In help.py, why did the file path need two backslashes in the code?

Answer:

A single backslash would be counted as special code, but a double backslash prints one of them.

### 8. In Step 5 you removed a quote mark. What did the error say, and did any of the program run? Why?

Answer:

The error says that paren was never closed. The program did not run. For syntax errors, Python reads the whole program and if it doesn't understand something, it stops.

## Part 3. Read the code

### 9. What does this program print? Write the output exactly.

```python
# Output: the title
print("-" * 5)
print("Hi\nthere")
# print("Bye")
```

Answer:

```
-----
Hi
there
```

Bye would not print.

### 10. This program has one mistake. What is it, and how would you fix it?

```python
# Output: a greeting
print("Welcome to the lab)
print("Have a good day")
```

Answer:

Add the end quote on line 2.
