from DList import *

names = DList()
numbers = DList()
emails = DList()
addresses = DList()


def search():
    print("\n---SEARCH---")
    print("1.  Name")
    print("2.  Phone Number")
    if input("SELECT(1~2): ") == 1:
        return
    else:
        return


def search(target):
    return


def register():
    print("\n---REGISTER---")
    while True:
        name = input("Name: ")
        if not is_number(name):
            if search(name) is not None:
                names.insert_after(names.head, name)
                break
            else:
                print("Already exists.")
        else:
            print("You input a wrong data.")
    while True:
        number = input("Number: ")
        if is_number(number):
            if search(number) is not None:
                numbers.insert_after(numbers.head, number)
                break
            else:
                print("Already exists.")
        else:
            print("You input a wrong data.")
    emails.insert_after(emails.head, input("Email: "))
    addresses.insert_after(addresses.head, input("Address: "))
    print("Processed.")


def delete():
    print("\n---SEARCH---")
    print("1.  Name")
    print("2.  Phone Number")
    if input("SELECT(1~2): ") == 1:
        return
    else:
        return


def is_number(number):
    for i in {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}:
        if i == number:
            return True
        else:
            return False


if __name__ == '__main__':
    while True:
        print("\n---Address Book---")
        print("1.  Search")
        print("2.  Register")
        print("3.  Delete")
        n = input("SELECT(1~3): ")
        if n == '1':
            search()
        elif n == '2':
            register()
        elif n == '3':
            delete()
        else:
            print("You input a wrong data.")
