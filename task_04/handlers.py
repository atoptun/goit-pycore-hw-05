from colorama import Fore, Back, Style, init
from functools import wraps
from typing import Callable
from exceptions import ContactNotFound


def input_error(func: Callable):
    @wraps(func)
    def wraper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError) as e:
            match func.__name__:
                case "cmd_add_contact" | "cmd_change_contact":
                    return f"{Fore.RED}Give me name and phone please."
                case "cmd_show_phone":
                    return f"{Fore.RED}Give me name please."
                case _:
                    return f"{Fore.RED}Enter the argument for the command"
        except ContactNotFound as e:
            return f"{Fore.RED}{e.strerror}"
        except Exception as e:
            return f"{Fore.RED}Error: {e}"
    return wraper

@input_error
def parse_input(line: str) -> tuple:
    """Returns a command and arguments"""
    cmd, *args = line.strip().split()
    return (cmd.strip().lower(), *args)


@input_error
def cmd_add_contact(contacts: dict, args: list[str]) -> str:
    """Command: add <name> <phone>"""
    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}Contact added."


@input_error
def cmd_change_contact(contacts: dict, args: list[str]) -> str:
    """Command: change <name> <phone>"""
    name, phone = args
    if name not in contacts:
        raise ContactNotFound("Contact not found.")
    contacts[name] = phone
    return f"{Fore.GREEN}Contact changed."


@input_error
def cmd_show_phone(contacts: dict, args: list[str]) -> str:
    """Command: phone <name>"""
    name = args[0]
    if name not in contacts:
        raise ContactNotFound("Contact not found.")
    return f"{Fore.GREEN}{name}: {Fore.BLUE}{contacts[name]}"


@input_error
def cmd_show_all(contacts: dict, args: list) -> str:
    """Command: all"""
    result = ""
    for name, phone in contacts.items():
        result += f"{Fore.GREEN}{name}: {Fore.BLUE}{phone}\n"
    return result
