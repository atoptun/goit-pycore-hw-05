from colorama import Fore, Back, Style, init
import handlers


init(autoreset=True)


def read_command() -> str:
    try:
        return input(f"{Fore.YELLOW}Command:{Fore.RESET} ")
    except KeyboardInterrupt:
        return "exit"

def main():
    print(f"{Fore.CYAN}Welcome to the assistant bot!")

    contacts = {}

    while True:
        cmd_str = read_command()
        if not cmd_str:
            continue
        command, *args = handlers.parse_input(cmd_str)

        match command:
            case "hello":
                print(f"{Fore.BLUE}How can I help you?")
            case "add":
                print(handlers.cmd_add_contact(contacts, args))
            case "change":
                print(handlers.cmd_change_contact(contacts, args))
            case "phone":
                print(handlers.cmd_show_phone(contacts, args))
            case "all":
                print(handlers.cmd_show_all(contacts, args))
            case "close" | "exit" | "quit":
                print(f"{Fore.GREEN}Have a nice day!")
                break
            case _:
                print(f"{Fore.RED}Invalid command.")


if __name__ == "__main__":
    main()
