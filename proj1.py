# This script goes through a text and gets some information about the text.
# Sample texts are in the task_template.py file

# load the template file
import task_template

# load libraries

# helpful vars
sep = "-" * 80

# Require username and password
username = input("username: ")
password = input("password: ")

# Go through the pairs and find if the user is registered, otherwise terminate the program
nr_users = len(task_template.user_name)
for user_index in range(nr_users):
    known_user = task_template.user_name[user_index]
    known_pass = task_template.user_password[user_index]
    if known_user == username and known_pass == password:
        break
    else:
        print("unregistered user, terminating the program..")
        quit()

print(f'{sep}\n'
      f'Welcome to the app, {username}.\n'
      f'We have {str(len(task_template.TEXTS))} texts to be analyzed.\n'
      f'{sep}')

# let the user select a text
selected_text = input("Enter a number btw. 1 and 3 to select: ")

# check if the number is between 1 and 3
if not int(selected_text) in range(1, 4):
    print("unknown text, terminating the program..")
    quit()

# save the text as a variable to be worked with
text = task_template.TEXTS[int(selected_text) - 1]

# get the results
results = {"nr_words": len(text.split()), "title": 0, "upper": 0, "lower": 0, "numbers": 0, "sum": 0}

for word in text.split():
    if word.istitle():
        results["title"] += 1

    if word.isupper() and word.isalpha():
        results["upper"] += 1

    if word.islower():
        results["lower"] += 1

    if word.isnumeric():
        results["numbers"] += 1
        results["sum"] = int(word) + results["sum"]

# get the data for the bar plot
word_length = {}
for word in text.split():
    length = len(word.strip(",.:;"))
    if length in word_length:
        word_length[length] += 1
    else:
        word_length[length] = 1

bar_width = max(word_length.values()) + 1

# print it all
print(f'{sep}\n'
      f'There are {results["nr_words"]} words in the selected text.\n'
      f'There are {results["title"]} titlecase words.\n'
      f'There are {results["upper"]} uppercase words.\n'
      f'There are {results["lower"]} lowercase words.\n'
      f'There are {results["numbers"]} numeric strings.\n'
      f'The sum of all the numbers is {results["sum"]}.\n'
      f'{sep}\n'
      f'LEN|{"OCCURENCES".center(bar_width)}|NR.\n'
      f'{sep}')

for key in sorted(word_length):
    print(f'{str(key).rjust(3)}|{str("*" * word_length[key]).ljust(bar_width)}|{word_length[key]}')
