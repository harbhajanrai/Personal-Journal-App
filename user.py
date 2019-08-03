import os
import journal

def setup():
    user_dir_name = "user"
    journals_dir_name = "journals"
    cwd = os.getcwd()
    user_path = cwd + "/" + user_dir_name
    journal_path = cwd + "/" + journals_dir_name
    try:
        if not os.path.exists(user_path):
            os.mkdir(user_path)
    except OSError:
        print("Creation of the directory failed")

    try:
        if not os.path.exists(journal_path):
            os.mkdir(journal_path)
    except OSError as e:
        print("Failed to setup Journal Folder")


def displayMenu():
    setup()
    status = input("Are you a registered user? y/n? ")
    if status == "y":
        login()
    elif status == "n":
        signup()


def login():
    username = input("Username : ")
    password = input("Password : ")
    cwd = os.getcwd()
    path = cwd + '/user/' + username
    print(path)
    # this check for username
    if os.path.exists(path):
        print("hello")
        file = open(path)
        data = file.readlines()
        # checks for password
        if password == data[1].strip() :
            print("Welcome Back")
            session(username)
        else:
            print("Sorry, Wrong Password ! Try Again")
            login()
        # now from here call joural part
    else:
        print("Sorry, User does not exist")
        login()


def signup():
    name = input("Your Name : ")
    username = input("Specify username for your account : ")
    password = input("Specify Password for your account : ")
    cwd = os.getcwd()
    user_info = cwd + '/user/' + username
    if os.path.exists(user_info):
        print("Username Already Taken, Please try again")
        signup()
    try:
        file = open(user_info, "w")
        file.write(username + "\n")
        file.write(password + "\n")
        file.write(name + "\n")
        session(username)
    except Exception as e:
        print(e)


# User session
def session(username):
    print("Welcome to your account " + username)
    author = username
    journal.controls(username)



if __name__== "__main__":
  displayMenu()
