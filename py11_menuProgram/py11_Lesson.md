# py11 Lesson: Menu Programs and Classes

You make a menu program that keeps running until the user picks Quit. You also learn what a class is, how to make objects from a class, and how to keep a list of objects, sort it, search it, and save it to a file.

## What to know

1. A menu loop prints a list of choices, asks the user to pick one, does that choice, and then shows the menu again. It keeps going until the user picks Quit.
2. break ends a loop right away. A menu can use while True: and then break when the user picks Quit.
3. Each menu choice gets its own function. That keeps main short and easy to read.
4. A class is a plan for a kind of object. It says what data each object holds and what each object can do. class Member: starts a class called Member. Class names start with a capital letter.
5. An object is one thing made from a class. Avery and Blake can be two Member objects. They follow the same plan, but each one holds its own data.
6. The data an object holds are called attributes. A member's name and points are attributes. You read an attribute with a dot: member.name.
7. The constructor is a function inside the class called __init__. It runs every time a new object is made. Member("Avery", 120) makes a new member and runs __init__, which stores the values with self.name = name and self.points = points.
8. self means this object. Inside the class, self.points is the points of whichever object is being used.
9. A method is a function inside a class. def add_points(self, amount): is a method. You call it on one object with a dot: member.add_points(50). Only that member's points change.
10. A method called __str__ returns the text for an object. Then print(member) prints that text, like Casey - 140 points.
11. A list can hold objects. members.append(Member("Jordan", 0)) adds a new member to the list. for member in members: loops through them.
12. sorted(members, key=lambda member: member.points, reverse=True) sorts the members by points, highest first. key tells sorted which attribute to compare. lambda member: member.points is a very short function that takes a member and gives back its points.
13. To search and ignore capital letters, make both sides lowercase: if text.lower() in member.name.lower():.
14. To load objects from a CSV file, read each line, split it, make an object from the parts, and append it to the list. To save, write the header line, then one line for each object.

## Step 1. Set up

1. Tell Claude: "Make a folder called py11_menuProgram in my repository folder."
2. On GitHub, open py11_Questions.md in this lesson folder. Activate Download raw file. Do the same for members.csv.
3. Tell Claude: "Move py11_Questions.md and members.csv from my Downloads folder into my py11_menuProgram folder."

## Step 2. First program: Club Manager

Tell Claude:

"Write a Python program called club.py and save it in my py11_menuProgram folder. Put a header comment at the top.

Make a Member class with a name and points, a constructor, an add_points method, and a str method that returns text like Casey - 140 points.

When the program starts, it loads members.csv into a list of Member objects and prints Loaded 3 members from members.csv. If the file is missing, it prints No members.csv found. Starting with an empty list.

Then it shows this menu and repeats it until Quit. The title is CLUB MANAGER. The choices are 1 Add member, 2 Record points, 3 Show leaderboard, 4 Search for a member, 5 Save, 6 Quit. Use get_int from my py10_errorHandling tickets.py for the choice, and get_text for names.

Add member asks for a name. If that name is already in the list, ignoring capital letters, it prints That member already exists. Otherwise it adds the member with 0 points.
Record points lists the members with numbers and their points, asks which member, asks points to add from 1 to 50, and prints the member's new total. If there are no members, it prints No members yet.
Show leaderboard prints the members sorted by points, highest first, in lined-up columns for Rank, Name, and Points.
Search asks for some text and prints every member whose name has that text in it, ignoring capital letters. If none match, it says so.
Save writes members.csv and a file called club_report.txt with a title, the date and time, and the leaderboard. Use try and except.
Quit prints Goodbye.

Each menu choice is its own function. Use a main function. Give every function and the class a comment. Put Input, Processing, and Output comments in the functions."

## Step 3. Run it

In the VS Code terminal, type: python club.py

You should hear Loaded 3 members, then the menu. Then do these, one at a time:

1. Choose 1. Add Jordan. You should hear Added Jordan.
2. Choose 1 again. Add avery in lowercase. You should hear That member already exists.
3. Choose 2. Pick Blake and add 50. You should hear Blake now has 145 points.
4. Choose 3. You should hear Blake 145, Casey 140, Avery 120, Jordan 0.
5. Choose 4. Search for CA. You should hear Casey. Search again for zz. You should hear that no members match.
6. Choose 5. You should hear that both files were saved.
7. Choose 6. You should hear Goodbye.

Tell Claude: "Read me members.csv." Blake should have 145 and Jordan should be on the list.

## Step 4. Explain

Tell Claude:

"Read me the Member class one line at a time. Tell me what self means each time it shows up."

Then ask Claude:

"What happens, step by step, when the program loads the line Avery,120 from members.csv?"

"When I add 50 points to Blake, how does the program change only Blake's points?"

"How does the leaderboard sort the members by points?"

"How does the menu loop end?"

## Step 5. Break it on purpose

Tell Claude:

"In club.py, change the add_points method so it says points = self.points + amount, without self in front of the first points. Do not run it yet."

Before you run it, say what you think Blake's points will be after you add 50. Then run it, choose 2, and add 50 to Blake. Then choose 3. Ask Claude:

"Why did Blake's points not change? What does self do in that line?"

Tell Claude to put self back. Run it again to make sure it works.

## Step 6. One more program

First say the plan: what attributes a book has, what the program does with the list of books, and what it prints. Then tell Claude to write it. Run it. Then ask Claude to walk you through the code.

shelf.py. A Book class with a title, an author, and a number of pages, and a str method that returns text like Holes by Louis Sachar, 233 pages. The program makes a list of 4 books typed into the program: Hatchet by Gary Paulsen, 195 pages. The Giver by Lois Lowry, 180 pages. Holes by Louis Sachar, 233 pages. Wonder by R. J. Palacio, 310 pages. It prints every book, the total pages, and the books sorted by pages with the most first. Then it asks for some text and prints every book whose author has that text in it, ignoring capital letters. You should hear a total of 918 pages, and the sorted list starting with Wonder. Search for lo. You should hear The Giver and Holes.

Ask Claude: "How is the Book class like the Member class? What is different?"

## Step 7. Make it yours

Have Claude write a program with a Track class. Each track has a title, a length in seconds, and a number of plays, and an add_play method that adds 1 to the plays. Make a list of 3 of your tracks. Call add_play on one track three times, then print every track. Before you run it, say what that track's plays will be. Then run it and check.

## Step 8. Answer the questions

Open py11_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py11 menu program and classes. Push.

## Turn in

All of these, pushed to your py11_menuProgram folder:

1. club.py, members.csv, club_report.txt, shelf.py, and your own program
2. py11_Questions.md with your answers
