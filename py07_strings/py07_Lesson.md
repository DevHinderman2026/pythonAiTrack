# py07 Lesson: Working with Text

You make three programs that work with text one character at a time. You learn how to pull pieces out of a string, how to check what kind of character something is, and how a secret code cipher works.

## What to know

1. A string is a row of characters. Letters, digits, spaces, and punctuation are all characters. Each one has an index starting at 0, the same as a list. word[0] is the first character. word[-1] is the last character.
2. len(word) gives the number of characters, including spaces.
3. A slice pulls out a piece of a string. word[0:3] gives the characters at index 0, 1, and 2. It stops before the second number, the same as range. word[2:] gives everything from index 2 to the end. word[::-1] gives the whole string backwards.
4. for ch in message: runs once for each character. Each time through, ch holds the next character.
5. These checks give back True or False: ch.isalpha() for a letter, ch.isupper() for a capital letter, ch.islower() for a lowercase letter, ch.isdigit() for a digit.
6. in checks if some text is inside other text. ch.lower() in "aeiou" is True if ch is a vowel, capital or not.
7. A string cannot be changed in place. message[0] = "X" causes an error. To change a string, build a new one: start with result = "", then add one character at a time with result = result + ch.
8. Every character has a number code. ord gives the code: ord("A") is 65 and ord("a") is 97. chr does the opposite: chr(66) is "B". Letters are in order, so B is 66, C is 67, and so on.
9. ord(letter) - ord("A") gives a capital letter's place in the alphabet, starting at 0. A is 0 and Z is 25.
10. The percent sign wraps numbers around. (25 + 3) % 26 is 2, so moving Z forward 3 places lands on C. It also works going backward: (2 - 3) % 26 is 25, so moving C back 3 places lands on Z.
11. A Caesar cipher is a secret code that moves every letter forward by the same number of places. Encoding moves forward. Decoding moves backward by the same number. Anything that is not a letter stays the same.
12. Useful string methods: upper() makes all capitals. lower() makes all lowercase. strip() removes spaces from the start and end. split() breaks a string into a list of words. replace(old, new) swaps one piece of text for another.

## Step 1. Set up

1. Tell Claude: "Make a folder called py07_strings in my repository folder."
2. On GitHub, open py07_Questions.md in this lesson folder. Activate Download raw file.
3. Tell Claude: "Move py07_Questions.md from my Downloads folder into my py07_strings folder."

## Step 2. First program: Secret Message

Tell Claude:

"Write a Python program called cipher.py and save it in my py07_strings folder. Put a header comment at the top. It is a Caesar cipher.

It asks Encode or decode, e or d, then Message, then Shift from 1 to 25.

Write these functions:
shift_letter takes one character and a shift. If it is a letter, it moves it by the shift, wraps around from Z to A, and keeps capitals as capitals and lowercase as lowercase. If it is not a letter, it gives it back the same.
encode takes a message and a shift and builds a new string by calling shift_letter on every character.
decode calls encode with a negative shift.
count_letters returns how many letters are in some text.
count_vowels returns how many vowels are in some text, capital or lowercase.

Print the result, then the number of letters and vowels in the message the user typed. Use a main function. Give every function a comment. Put Input, Processing, and Output comments in main."

## Step 3. Run it

In the VS Code terminal, type: python cipher.py

Type e, then Meet me at 3:00!, then 3. You should hear Result: Phhw ph dw 3:00! and Letters 8, Vowels 4.

Run it again. Type d, then Phhw ph dw 3:00!, then 3. You should hear the original message back.

## Step 4. Explain

Tell Claude:

"Read me shift_letter one line at a time. Then trace it for me with the letter y and a shift of 3. Tell me every number it works out along the way."

Then ask Claude:

"How does encode build the new string?"

"How does decode work if it only calls encode?"

"Why do the 3, the colon, and the spaces stay the same?"

## Step 5. Break it on purpose

Tell Claude:

"In cipher.py, take out the percent 26 wrap-around in shift_letter. Do not run it yet."

Before you run it, think about what happens when you encode xyz with a shift of 3. Will it still give letters? Then run it. Ask Claude:

"What characters came out, and why? What does the percent 26 do?"

Tell Claude to put the wrap-around back. Run it again with xyz and 3. You should hear abc.

## Step 6. Two more programs

For each program, first say the plan: what the program looks at in the text, and what it builds or counts. Then tell Claude to write it. Run it with the test answers. Then ask Claude to walk you through the code.

1. names.py. It asks for a full name with a first and last name, like jordan lee. It cleans up extra spaces with strip and splits the name into two words. It prints the name as Last, First with capital first letters, like Lee, Jordan. Then it prints the initials, like J.L. Test it with jordan lee, with a couple of extra spaces before it. You should hear Lee, Jordan and J.L.

2. textcheck.py. It asks for a sentence. It counts the capital letters, lowercase letters, digits, and everything else, like spaces and punctuation. It prints the four counts, then prints the sentence backwards in all capitals. Test it with Room 112 is open. You should hear 1 capital, 9 lowercase, 3 digits, 3 other, and NEPO SI 211 MOOR.

For names.py, ask Claude: "What does split give back, and how did you get the first and last name out of it?"

For textcheck.py, ask Claude: "How did you print the sentence backwards?"

## Step 7. Make it yours

Have Claude write a program that asks for a track title and makes a file name out of it: all lowercase, spaces turned into underscores, and .mp3 on the end. For example, Night Drive becomes night_drive.mp3. Before you run it, pick a title and say what the file name should be. Then run it and check.

## Step 8. Answer the questions

Open py07_Questions.md in VS Code. Type your answer under each question. Use your own words. Do not have Claude write the answers. Save the file.

## Step 9. Push

Commit with the summary py07 strings. Push.

## Turn in

All of these, pushed to your py07_strings folder:

1. cipher.py, names.py, textcheck.py, and your own program
2. py07_Questions.md with your answers
