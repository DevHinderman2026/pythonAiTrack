# py05 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py05_functions folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. What is the difference between defining a function and calling it?

Answer:

### 2. What is the difference between a parameter and an argument?

Answer:

### 3. What does return do? What is the difference between return and print?

Answer:

### 4. What is a local variable? How does a value get into a function and back out?

Answer:

### 5. What goes in a function comment?

Answer:

### 6. What is the main function for, and how does it get started?

Answer:

## Part 2. Your programs

### 7. In snack2.py, trace what happens when the program figures out the tax. Which function calls which, and what values go in and come back?

Answer:

### 8. In Step 5 you changed return to print. What happened, and why?

Answer:

## Part 3. Read the code

### 9. What does this program print? Write the output exactly.

```python
def double(number):
    """Purpose: doubles a number. Parameter: number. Returns: number times 2."""
    return number * 2

def main():
    # Processing
    a = double(3)
    b = double(a)
    # Output
    print(a, b)

if __name__ == "__main__":
    main()
```

Answer:

### 10. This program does not print what the writer wanted. What does it print, and how would you fix it?

```python
def add_tax(price):
    """Purpose: adds 10 percent tax. Parameter: price. Returns: nothing."""
    total = price * 1.10

def main():
    add_tax(20)
    print(total)

if __name__ == "__main__":
    main()
```

Answer:
