# py06 Questions

Type your answer on the line under each question. Use your own words. One to three sentences is enough. Save this file in your py06_listsAndArrays folder and push it with your programs.

Answer these yourself. You can run code to check an answer after you write it.

## Part 1. How Python works

### 1. What is a list? Why is it better than making a separate variable for every score?

Answer:

### 2. What is an index? What index does the first item have? What index does the last item have in a list of 10 items?

Answer:

### 3. What does append do?

Answer:

### 4. What is the difference between `for score in scores` and `for i in range(len(scores))`? When would you use each one?

Answer:

### 5. What is the difference between sorted(scores) and scores.sort()?

Answer:

## Part 2. Your programs

### 6. In your own words, explain how find_highest finds the highest score.

Answer:

### 7. In Step 5 the lowest started at 0. What did the program print, and why?

Answer:

### 8. In weather.py, how did the program turn an index into a day number?

Answer:

## Part 3. Read the code

### 9. What does this program print? Write the output exactly.

```python
# Processing
tracks = ["Intro", "Night Drive", "Echoes", "Outro"]
tracks.append("Bonus")
tracks[1] = "Late Drive"
# Output
print(len(tracks))
print(tracks[1])
print(tracks[4])
```

Answer:

### 10. What does this program print? Write the output exactly.

```python
# Processing: count the big numbers
numbers = [4, 12, 7, 15, 9]
count = 0
for n in numbers:
    if n > 8:
        count = count + 1
# Output
print(count)
```

Answer:

### 11. This line causes an error. What is the error, and why?

```python
scores = [70, 80, 90]
print(scores[3])
```

Answer:
