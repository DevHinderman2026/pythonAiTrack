# py07 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py07_strings folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. How is a string like a list?

Answer:

### 2. What does a slice do? What does word[0:3] give you?

Answer:

### 3. A string cannot be changed in place. So how does a program make a changed version of a string?

Answer:

### 4. What do ord and chr do?

Answer:

### 5. What does the percent sign do in the cipher? Why is it needed?

Answer:

## Part 2. Your programs

### 6. Explain how shift_letter turns y into b with a shift of 3. Use the numbers.

Answer:

### 7. How does decode work by calling encode?

Answer:

### 8. In Step 5 you took out the wrap-around. What did xyz turn into, and why?

Answer:

## Part 3. Read the code

### 9. What does this program print? Write the output exactly.

```python
# Processing
word = "Python"
# Output
print(word[0])
print(word[-1])
print(word[1:4])
print(len(word))
```

Answer:

### 10. What does this program print? Write the output exactly.

```python
# Processing: build a new string
message = "a1b2"
result = ""
for ch in message:
    if ch.isdigit():
        result = result + "#"
    else:
        result = result + ch.upper()
# Output
print(result)
```

Answer:
