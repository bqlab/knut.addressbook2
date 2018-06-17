from DList import *


def search():
    if book.is_empty():
        print("Nothing registered.")
        return None
    while True:
        print("\n---SEARCH---")
        target_pos = locate(input("Input: "))
        if target_pos is None:
            print("Cannot Found.")
            return None
        else:
            target = book.head.next
            for i in range(0, target_pos, 1):
                target = target.next
            target.item.print_list()
            return target


def locate(target):
    target_pos = 0
    if book.is_empty():
        return None
    else:
        p = book.head.next
        if not is_number(target):
            while p != book.tail:
                if p.item.head.next.item == target:
                    return target_pos
                target_pos += 1
                p = p.next
        else:
            while p != book.tail:
                if p.item.head.next.next.item == target:
                    return target_pos
                target_pos += 1
                p = p.next
        return None


def register():
    p = DList()
    print("\n---REGISTER---")
    while True:
        name = input("Name(Up to 20): ")
        if not is_number(name) and len(name) <= 20:
            if locate(name) is None:
                p.insert_before(p.tail, name)
                break
            else:
                print("Already exists.")
        else:
            print("You input a wrong data.")
    while True:
        number = input("Number(Up to 11): ")
        if is_number(number) and len(number) <= 11:
            if locate(number) is None:
                p.insert_before(p.tail, number)
                break
            else:
                print("Already exists.")
        else:
            print("You input a wrong data.")
    while True:
        email = input("Email(Up to 100): ")
        if '@' in email and len(email) <= 100:
            p.insert_before(p.tail, email)
            break
        else:
            print("You input a wrong data.")
    while True:
        address = input("Address(Up to 100): ")
        if len(address) <= 100:
            p.insert_before(p.tail, address)
            break
        else:
            print("You input a wrong data.")
    book.insert_before(book.tail, p)
    print("Processed.")


def modify():
    target = search()
    if target is None:
        return
    else:
        answer = input("Modify[Y/N]: ")
        if answer == 'Y' or answer == 'y':
            print("1.  Name")
            print("2.  Number")
            print("3.  Email")
            print("4.  Address")
            n = input("SELECT(1~4): ")
            if n == '1':
                while True:
                    name = input("Name(Up to 20): ")
                    if not is_number(name) and len(name) <= 20:
                        if locate(name) is None or name is target.head.next.item:
                            target.item.head.next.item = name
                            print("Processed.")
                            break
                        else:
                            print("Already exists.")
                    else:
                        print("You input a wrong data.")
            elif n == '2':
                while True:
                    number = input("Number(Up to 11): ")
                    if is_number(number) and len(number) <= 11:
                        if locate(number) is None or number is target.head.next.next.item:
                            target.item.head.next.next.item = number
                            print("Processed.")
                            break
                        else:
                            print("Already exists.")
                    else:
                        print("You input a wrong data.")
            elif n == '3':
                while True:
                    email = input("Email(Up to 100): ")
                    if '@' in email and len(email) <= 100:
                        target.item.head.next.next.next.item = email
                        print("Processed.")
                        break
                    else:
                        print("You input a wrong data.")
            elif n == '4':
                while True:
                    address = input("Address(Up to 100): ")
                    if len(address) <= 100:
                        target.item.head.next.next.next.next.item = address
                        print("Processed.")
                        break
                    else:
                        print("You input a wrong data.")
            else:
                print("You input a wrong data.")
        else:
            print("Canceled.")


def delete():
    target = search()
    if target is None:
        return
    else:
        answer = input("Delete[Y/N]: ")
        if answer == 'Y' or answer == 'y':
            f = target.prev
            r = target.next
            f.next = r
            r.prev = f
            book.size -= 1
            print("Processed.")
        else:
            print("Canceled.")


def is_number(number):
    for i in number:
        if not i in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            return False
    return True


if __name__ == '__main__':
    while True:
        print("\n---Address Book---")
        print("1.  Search")
        print("2.  Register")
        print("3.  Modify")
        print("4.  Delete")
        n = input("SELECT(1~4): ")
        if n == '1':
            search()
        elif n == '2':
            register()
        elif n == '3':
            modify()
        elif n == '4':
            delete()
        else:
            print("You input a wrong data.")