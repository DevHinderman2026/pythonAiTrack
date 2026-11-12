# py09 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py09_files folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. What is a CSV file? What is usually on the first line?

Answer:

### 2. What is a relative path? Why is it better than a full path that starts with C?

Answer:

### 3. What does with open do, and when does the file get closed?

Answer:

### 4. What does split(",") do to a line from a CSV file? Why do the numbers still need int?

Answer:

### 5. What is the difference between opening a file with "w" and with "a"?

Answer:

## Part 2. Your programs

### 6. In read_scores, explain what happens to the line for Avery, step by step, until it is a name and a row of numbers.

Answer:

### 7. What did filescores.py do when scores.csv was missing? How does it know the file is missing?

Answer:

### 8. In Step 5 you changed w to a and ran it twice. What did report.txt look like, and why?

Answer:

## Part 3. Read the code

### 9. A file called pets.csv has these three lines:

```text
Name,Age
Rex,4
Milo,2
```

What does this program print? Write the output exactly.

```python
# Input and Output: read the file, skip the header
with open("pets.csv", "r") as file:
    file.readline()
    for line in file:
        parts = line.strip().split(",")
        print(parts[0], "is", parts[1])
```

Answer:

### 10. What will be in the file notes.txt after this program runs? Write the file exactly.

```python
# Output: write to a file
with open("notes.txt", "w") as out_file:
    out_file.write("First")
    out_file.write("Second\n")
    out_file.write("Third\n")
```

Answer:
