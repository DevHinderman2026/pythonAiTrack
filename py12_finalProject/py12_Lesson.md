# py12 Lesson: Final Project

You plan and build one bigger program that uses what you learned in py01 through py11. This time you write the plan first, then have Claude build the program one function at a time. After each function, you run it and explain it before you go on.

This lesson takes more than one class. Push your work at the end of every class.

## What to know

1. A bigger program is easier to build one piece at a time. Build a small piece, run it, make sure it works, then add the next piece. If something breaks, you know it was the last piece you added.
2. Start with a skeleton. A skeleton is a program that has main and the function names, but the functions do not do much yet. It runs from the first day, and every piece you add makes it do more.
3. A plan says what the program does in order, what data it stores and how, and what functions it needs. For each function, the plan says what goes in and what comes back.
4. A test plan is a list of answers to try, written before you run the program. It has good answers, wrong answers, and answers right at the edges. For each one, it says what should happen.
5. If you can explain what a function does, what goes in, and what comes back, you understand it. If you cannot, ask Claude about it before you add the next piece.

## Step 1. Set up

1. Tell Claude: "Make a folder called py12_finalProject in my repository folder."
2. On GitHub, open py12_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py12_Questions.md from my Downloads folder into my py12_finalProject folder."

## Step 2. Pick a project

Pick one.

Option A. Quiz Tracker. A club took 3 quizzes and needs a score report.

1. Ask how many members, a whole number from 1 to 6. Ask again on anything else.
2. Ask each member's name. Names cannot be blank.
3. Ask each member's score on each of the 3 quizzes, a whole number from 0 to 100.
4. Store the names and scores so the program can loop over them.
5. Print a leaderboard sorted by total, highest first, with each member's name, total, and average with 2 decimal places, in lined-up columns.
6. Print the top scorer, and the hardest quiz, which is the quiz with the lowest average.
7. Write the leaderboard and those two lines to quiz_results.txt, with the date and time at the top.

Option B. Your own program. It can be about your music or anything else. It must have all of these:

1. Input that is checked, using get_int, get_text, or get_yes_no.
2. A list of lists or a list of objects.
3. At least one total or average.
4. A sorted report printed on the screen.
5. A report file with the date and time at the top.
6. A main function and at least 4 other functions.

If you pick Option B, tell Mr. McMaster your idea before you start the plan.

## Step 3. Write the plan

Open py12_Questions.md in VS Code. Answer Part 1, the plan, yourself. Do not have Claude write it. Save the file and push it before you build anything.

You can ask Claude questions while you plan, like "Would a list of lists or a list of objects work better for this?" But the plan is in your words.

## Step 4. Build the skeleton

Tell Claude:

"Read my plan in py12_Questions.md in my py12_finalProject folder. Make a program called project.py in the same folder. Put a header comment at the top. Make a main function and every function in my plan, with a comment for each one, but have each function only print its own name for now. main calls them in the order in my plan. End the file with the main guard."

Run it with python project.py. You should hear each function name, in the order in your plan.

## Step 5. Build one function at a time

Pick the first function in your plan. Tell Claude:

"In project.py, write the real code for [function name] only. It should [what your plan says it does]. Do not change any other function."

Then do these three things before you go on:

1. Run it. Make sure it works. If it asks for input, try a good answer and a wrong one.
2. Tell Claude: "Read me [function name] one line at a time and tell me what each line does."
3. Say back to Claude, in your own words, what the function does, what goes in, and what comes back. Ask Claude if you got it right.

Then move to the next function. Do this for every function in your plan. If you need a function that is not in your plan, add it to the plan first.

## Step 6. Test

Run the program with every answer in your test plan. For each one, check that what happened matches what you wrote. If something is wrong, tell Claude what you typed, what you expected, and what happened. Have it fix the code, then test again.

For Option A, one test: 2 members. Jordan with 90, 85, 90. Sam with 80, 70, 91. You should hear Jordan first with 265 and 88.33, Sam with 241 and 80.33, Jordan as top scorer, and quiz 2 as the hardest quiz.

When it all works, tell Claude: "Read me the report file."

## Step 7. Explain the whole program

Tell Claude:

"Read me main in project.py one line at a time. After each line, tell me which function it calls and what that function gives back."

Then tell Claude:

"Ask me five questions about how my program works, one at a time. Wait for my answer each time. Tell me if I got it right, and if not, explain it."

## Step 8. Answer the questions

Open py12_Questions.md in VS Code. Answer Part 2 and Part 3. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py12 final project. Push.

## Turn in

All of these, pushed to your py12_finalProject folder:

1. project.py and the report file it makes
2. py12_Questions.md with your plan and your answers
