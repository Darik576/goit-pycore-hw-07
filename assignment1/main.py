from models import AddressBook
from parser import parse_input
from handlers import (
    add_contact, change_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays
)


def show_help():
    return (
        "Available commands:\n"
        "hello - show greeting\n"
        "add name phone - add new contact or add phone to existing contact\n"
        "change name old_phone new_phone - change existing phone number\n"
        "phone name - show all phone numbers for contact\n"
        "all - show all contacts\n"
        "add-birthday name DD.MM.YYYY - add birthday to contact\n"
        "show-birthday name - show contact's birthday\n"
        "birthdays - show birthdays in the next 7 days\n"
        "exit / close - exit the program"
    )


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "help":
            print(show_help())

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
