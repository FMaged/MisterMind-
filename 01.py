import os
import random
import sys

COLORS = ["R", "B", "G", "Y", "C", "P"]
CODE_LENGHT = 4
ATTEMPTS = 10


def begrussen(Colors: list, Code_Length, Attempts):
    print(Colorize("Welcome to MisterMind!", "G"))
    print("The goal is to guess the Secret COLORE")
    print("The Code is made up of the following COLORS", Colorized_list(Colors))
    print("The Secret code constists of ", Code_Length, " Colors")
    print("you Have ", Attempts, " Attempts to guess the secret code.")
    print("Enter your guess as a continous string of letters, e,g. '" + Colorized_list(Colors[0:4]) + "'")


def Support_Colors():
    if sys.platform.startswith("win"):
        return True
    return os.getenv("TERM") in ("xterm", "xterm-color", "xterm-256color", "linux", "screen")


def Colorize(text: str, Color: str) -> str:
    if not Support_Colors():
        return text

    Colors = {
        "R": "\033[91m",
        "B": "\033[94m",
        "G": "\033[92m",
        "Y": "\033[93m",
        "C": "\033[36m",
        "P": "\033[95m",
        "WE": "\033[37m",
        "BK": "\033[30m",
        "RESET": "\033[0m",
    }
    # return f"{Colors.get(Color,Colors['RESET'])}{text}{Colors['RESET']}"
    return Colors.get(Color, "") + text + Colors["RESET"]


def uberprufen(Colors, Code_Length):
    Same = False
    Guess = ""
    while not len(Guess) == Code_Length or not Same:
        Guess = input()
        if not len(Guess) == Code_Length:
            print(
                Colorize(
                    ("please Enter a Guess with only " + str(Code_Length) + " Colors. Your entered ")
                    + str(len(Guess))
                    + " Colors",
                    "R",
                )
            )

        Guess = list(Guess.upper())
        Same = True
        for Color in Guess:
            if Color not in Colors:
                Same = False
                print(Colorize("please enter a string that contains " + "".join(Colors[0:4]), "R"))
                # Guess = ""
                break

    return Guess


def CalculateMatches(Secret_Code, GuessList):
    schwarz = 0
    weiss = 0
    for i in range(CODE_LENGHT):
        if GuessList[i] == Secret_Code[i]:
            schwarz += 1
        Set_Secret_Code = set(Secret_Code)
        if GuessList[i] in Set_Secret_Code:
            weiss += 1
    return schwarz, weiss - schwarz


def generate_Secrate_Code(Colors, code_Lenght):
    print("DEBUG: Generating secret code ....", Colorized_list(Colors), code_Lenght)
    return random.choices(COLORS, k=code_Lenght)

    # myList = []
    # for i in range(code_Lenght):
    #     myList.append(random.choice(Colors))

    # return myList


def Colorized_list(list):
    Colorized_list = []
    for char in list:
        Colorized_list.append(Colorize(char, char))
    return "".join(Colorized_list)


def play_Game():
    secret_Code = generate_Secrate_Code(COLORS, CODE_LENGHT)
    print("DEBUG: Secret Code: ", Colorized_list(COLORS))
    print("Enter your guess: ")
    for i in range(ATTEMPTS):
        GuessList = uberprufen(COLORS, CODE_LENGHT)
        schwarz, weiss = CalculateMatches(secret_Code, GuessList)
        Colorized_list_Str = Colorized_list(GuessList)
        print("Attempt", i + 1, Colorized_list_Str, "schwarz:", schwarz, " Weiss: ", weiss)
        if schwarz == 4:
            print(Colorize("YOU WON!", "G"))
            return
        if i == ATTEMPTS:
            print(Colorize("YOU LOSE", "R"))
            return


if __name__ == "__main__":
    begrussen(COLORS, CODE_LENGHT, ATTEMPTS)

    play_Game()
