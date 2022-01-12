# This script goes through a text and gets some information about the text.
# Sample texts are in the task_template.py file

# load the template file
import task_template

# load libraries

# helpful vars
sep = "-" * 20

# Require username and password
username = input("username: ")
password = input("password: ")

# Go through the pairs and find if the user is registered, otherwise terminate the program
nr_users = len(task_template.user_name)
for user_index in range(nr_users):
    known_user = task_template.user_name[user_index]
    known_pass = task_template.user_password[user_index]
    if known_user == username.lower() and known_pass == password:
        break
    else:
        print("unregistered user, terminating the program..")
        quit()

print(sep + "\n"
      + "Welcome to the app, " + username + "\n"
      + "We have " + str(len(task_template.TEXTS)) + " texts to be analyzed." + "\n"
      + sep + "\n")


