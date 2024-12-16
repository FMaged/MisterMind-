import os
import platform


def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")  # Clear command for Windows
    else:
        os.system("clear")  # Clear command for macOS/Linux


def readInt() -> int:
    while True:
        try:
            number = int(input("Enter an integer: "))
            return number
        except ValueError:
            print("Invalid int, please enter again!")
            return -1


def readIntBetween(From: int, To: int) -> int:
    num = readInt()
    while num < From or num > To:
        print(f"Enter an Int Between [{From} - {To}]\n")
        num = readInt()
    return num


def readSpecificChars(CharList: list, text: str) -> list:
    List = ""
    while not len(List) == len(CharList) - 2:
        List = input(f"{'':<{55 - (len(text) / 5)}}{text}")

        List = list(List.upper())
        for Char in List:
            if Char not in CharList:
                List = ""
                break

    return List
