# parsingAlgorithm
A parsing algorithm in python

Python can automate log analysis and security tasks by combining file handling, parsing, and algorithm development. This example demonstrates how to build a suspicious login detection algorithm to identify users with three or more failed login attempts.

Steps to Build the Algorithm
1.	Understand the Input: 
o	Input Structure: A .txt log file with one username per line, where each entry represents a failed login attempt.
o	Goal: For every login, check the number of failed attempts for the user and return an alert if they have three or more failed attempts.

1. Import and Parse the Log File:
•	Open the file using the open() function with the mode "r" for reading.
•	Use the .read() method to load the file content as a string.
•	Apply the .split() method to separate the string into a list of usernames.
Example:
with open("login_attempts.txt", "r") as file:
    file_content = file.read()
    usernames = file_content.split()  # Parse file into a list of usernames

2. Counting Username Occurrences:
•	Use a for loop to iterate over the list.
•	Maintain a counter variable to track how many times the target username appears.
•	Increment the counter each time the username matches the target.
Example:
counter = 0
target_user = "eraab"
for user in usernames:
    if user == target_user:
        counter += 1

3. Define the Function:
•	Create a reusable function to: 
o	Accept a list of usernames (login_list) and the current user (current_user) as arguments.
o	Count occurrences of current_user in login_list.
o	Print an alert if the count is three or more; otherwise, allow login.
Example:
def login_check(login_list, current_user):
    counter = 0
    for user in login_list:
        if user == current_user:
            counter += 1
    if counter >= 3:
        print(f"Account locked for user: {current_user}")
    else:
        print(f"User {current_user} can log in.")

4. Run the Function:
•	Test the function on specific usernames from the log.
•	Example: 
login_check(usernames, "elarson")  # Output: User elarson can log in.
login_check(usernames, "eraab")   # Output: Account locked for user: eraab
