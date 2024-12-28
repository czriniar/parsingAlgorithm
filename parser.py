# Import and parse the log file
with open("login_attempts.txt", "r") as file:
    file_content = file.read()
    usernames = file_content.split()

# Define the login check function
def login_check(login_list, current_user):
    counter = 0  # Initialize the counter
    for user in login_list:  # Iterate through the list
        if user == current_user:  # Check for matches
            counter += 1
    if counter >= 3:  # Decision logic
        print(f"Account locked for user: {current_user}")
    else:
        print(f"User {current_user} can log in.")

# Test the function
login_check(usernames, "elarson")  # Example user
login_check(usernames, "eraab")   # Example user with multiple failed attempts
