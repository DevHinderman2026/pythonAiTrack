# py10 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py10_errorHandling folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. What is an exception? What happens if a program does not handle one?

Answer:

### 2. How do you read a traceback? Where do you find the type of error?

Answer:

### 3. What do try and except do?

Answer:

### 4. Why is it better to write except ValueError than a plain except?

Answer:

### 5. What is a reusable input function? Why is it useful?

Answer:

## Part 2. Your programs

### 6. In crash.py, what type of error did you get when you typed two, and which line caused it?

Answer:

### 7. Explain how get_int keeps asking until it gets a good answer, and how it stops.

Answer:

### 8. In Step 6 you moved the int line above the try. What happened, and why?

Answer:

### 9. In average.py, what would cause a ZeroDivisionError, and what does the program do about it?

Answer:

## Part 3. Read the code

### 10. The user types 7. What does this program print? Then answer again if the user types seven.

```python
# Input and Output
try:
    count = int(input("Count: "))
    print("You typed", count)
except ValueError:
    print("Not a whole number")
print("Done")
```

Answer:

### 11. What does this program print? Write the output exactly.

```python
# Processing and Output
numbers = [3, 0, 5]
for n in numbers:
    try:
        print(10 // n)
    except ZeroDivisionError:
        print("Skip")
```

Answer:
