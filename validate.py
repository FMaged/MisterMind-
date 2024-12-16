import os
import platform

import Global
import Logik


def clear_terminal() -> None:
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


def readSpecificChars(CharList: list, Len_Chois: int, text: str) -> list:
    List = ""
    while not len(List) == Len_Chois:
        List = input(f"{'':<{55 - (len(text) / 5)}}{text}")
        if not len(List) == CharList:
            Logik.printt(
                Logik.Colorize(
                    ("please Enter a Guess with only " + str(Global.Chois) + " Colors. Your entered ")
                    + str(len(List))
                    + " Colors",
                    "R",
                )
            )
        List = list(List.upper())
        for Char in List:
            if Char not in CharList:
                List = ""
                Logik.printt(
                    Logik.Colorize(
                        "please enter a string that contains " + "".join(Global.COLORS[0 : Global.Chois]), "R"
                    )
                )
                break

    return List
