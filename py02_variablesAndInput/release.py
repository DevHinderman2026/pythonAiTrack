# Name: Russell Hinderman
# Date: November 19, 2026
# Program: release.py
# Description: Figures out the total length of a music release in hours and minutes.

MINUTES_PER_HOUR = 60

# Input
title = input("Release title: ")
tracks = int(input("Number of tracks: "))
average_length = float(input("Average track length in minutes: "))

# Processing
total_minutes = round(tracks * average_length)
hours = total_minutes // MINUTES_PER_HOUR
minutes = total_minutes % MINUTES_PER_HOUR

# Output
print()
print(f"Release Length for {title}")
print(f"Tracks: {tracks}")
print(f"Total length: {hours} hours {minutes} minutes")
