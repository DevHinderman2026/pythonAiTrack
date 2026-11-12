# py08 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py08_nestedData folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. What is a list of lists? How is it like a table?

Answer:

### 2. In scores[2][1], which number is the row and which is the column? Which row and column is that, counting from 1?

Answer:

### 3. In a nested loop, how many times does the inside loop run?

Answer:

### 4. What are parallel lists? What goes wrong if you sort one and not the other?

Answer:

### 5. What is a dictionary? What is a key and what is a value?

Answer:

### 6. In your own words, how does a bubble sort work?

Answer:

## Part 2. Your programs

### 7. In scoreboard.py, how does the program find the average for one round?

Answer:

### 8. In Step 5 the sort did not move the names. What happened to the table?

Answer:

## Part 3. Read the code

### 9. What does this program print? Write the output exactly.

```python
# Processing: 2 rows, 3 columns
table = [[4, 7, 1],
         [2, 9, 5]]
# Output
print(table[0][1])
print(table[1][2])
print(len(table))
```

Answer:

### 10. What does this program print? Write the output exactly.

```python
# Processing and Output: a total for each row
table = [[1, 2], [3, 4], [5, 6]]
for row in table:
    total = 0
    for value in row:
        total = total + value
    print(total)
```

Answer:

### 11. What does this program print? Write the output exactly.

```python
# Processing
plays = {"Intro": 10, "Outro": 4}
plays["Echoes"] = 7
plays["Intro"] = plays["Intro"] + 1
# Output
print(plays["Intro"])
print(len(plays))
```

Answer:
