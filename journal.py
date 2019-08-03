import datetime
import os


def create_journal(username):
    name = input("Name your journal:   ")

    cwd = os.getcwd()
    path = cwd + "/journals/" + username
    os.mkdir(path)
    path = path + "/" +name

    try:
        if not os.path.exists(path):
            os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)


def open_journal(username):
    cwd = os.getcwd()
    path = cwd + "/journals/" + username
    journal_list = os.listdir(path)

    print("Current Journals: " + str(len(journal_list)))
    for journal in journal_list:
        print(journal)

    name = input("Name of journal:  ")
    cwd = os.getcwd()
    path = cwd + "/journals/" + username + "/" + name

    directory_list = os.listdir(path)
    print("Current Entries: " + str(len(directory_list)))
    for entry in directory_list:
        print(entry)


def select_journal(username):
    cwd = os.getcwd()
    path = cwd + "/journals/" + username
    journal_list = os.listdir(path)

    print("Current Journals: " + str(len(journal_list)))
    for journal in journal_list:
        print(journal)


def fetch_content(username):
    content = input("Write till your heart's content :)")
    return content


def add_page(username):
    title = input("Name your entry:  ")
    filename = title.replace(" ", "") + ".txt"  # Adding .txt so we can create the page

    add_content(username)


def remove_page(username):
    cwd = os.getcwd()
    path = cwd + "/journals/" + username
    journal_list = os.listdir(path)

    print("Current Journals: " + str(len(journal_list)))
    for journal in journal_list:
        print(journal)

    name = input("Name of journal:  ")
    cwd = os.getcwd()
    path = cwd + "/journals/" + username + "/" + name

    directory_list = os.listdir()
    print("Current Entries: " + str(len(directory_list)))
    for entry in directory_list:
        print(entry)

    title = input("What's the title of your entry?  ")
    filename = path + "/" + title + ".txt"
    os.remove(filename)


def controls(username):
    print("What would you like to do?: ")
    print("1: Create a journal")
    print("2: Open a journal")
    print("3: Create an entry")
    print("4: Remove an entry")
    option = input("Your choice:  ")
    print("-----\n-----")

    if option == "1" or option == 1:
        create_journal(username)
    elif option == "2" or option == 2:
        open_journal(username)
    elif option == "3" or option == 3:
        add_page(username)
    elif option == "4" or option == 4:
        remove_page(username)
    else:
        print("Please answer based on your choices")
        controls(username)

    choice = input("Do you need to do anything else? (y/n)")
    if choice == "y" or choice == "yes":
        controls(username)
    else:
        print("See you later!")