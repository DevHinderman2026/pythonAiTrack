# py11 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py11_menuProgram folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. How does a menu loop work? How does it end?

Answer:

### 2. What is the difference between a class and an object?

Answer:

### 3. What is an attribute? What is a method? Give one example of each from club.py.

Answer:

### 4. What does the constructor do, and when does it run?

Answer:

### 5. What does self mean inside a class?

Answer:

### 6. How does the program search for a name and ignore capital letters?

Answer:

## Part 2. Your programs

### 7. What happens, step by step, when club.py loads the line Avery,120 from members.csv?

Answer:

### 8. In Step 5 you took self out of add_points. What happened to Blake's points, and why?

Answer:

### 9. Why does each menu choice in club.py get its own function?

Answer:

## Part 3. Read the code

### 10. What does this program print? Write the output exactly.

```python
class Counter:
    """A counter that starts at a number and can go up."""

    def __init__(self, start):
        """Purpose: makes a counter. Parameter: start. Returns: nothing."""
        self.value = start

    def add_one(self):
        """Purpose: adds 1 to this counter. Returns: nothing."""
        self.value = self.value + 1

# Processing
a = Counter(5)
b = Counter(10)
a.add_one()
a.add_one()
b.add_one()
# Output
print(a.value, b.value)
```

Answer:

### 11. What does this program print? Write the output exactly.

```python
class Pet:
    """A pet with a name."""

    def __init__(self, name):
        """Purpose: makes a pet. Parameter: name. Returns: nothing."""
        self.name = name

    def __str__(self):
        """Purpose: gives the text for this pet. Returns: text."""
        return "Pet: " + self.name

# Processing and Output
pets = [Pet("Rex"), Pet("Milo")]
for pet in pets:
    print(pet)
```

Answer:
