import os
import random
import sys

import Global
import validate


def Support_Colors() -> bool:
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


def Colorized_list(list):
    Colorized_list = []
    for char in list:
        Colorized_list.append(Colorize(char, char))
    return "".join(Colorized_list)


def generate_Secrate_Code(Colors, code_Lenght):
    print("DEBUG: Generating secret code ....", Colorized_list(Colors), code_Lenght)
    return random.choices(Global.COLORS, k=code_Lenght)


def CalculateMatches(Secret_Code, GuessList):
    schwarz = 0
    weiss = 0
    for i in range(Global.CODE_LENGHT):
        if GuessList[i] == Secret_Code[i]:
            schwarz += 1
        Set_Secret_Code = set(Secret_Code)
        if GuessList[i] in Set_Secret_Code:
            weiss += 1
    return schwarz, weiss - schwarz


def play_Game():
    secret_Code = generate_Secrate_Code(Global.COLORS, Global.CODE_LENGHT)
    print("DEBUG: Secret Code: ", Colorized_list(secret_Code))
    print("Enter your guess: ")
    for i in range(Global.ATTEMPTS):
        GuessList = validate.readSpecificChars(Global.COLORS)
        schwarz, weiss = CalculateMatches(secret_Code, GuessList)
        Colorized_list_Str = Colorized_list(GuessList)
        print("Attempt", i + 1, Colorized_list_Str, "schwarz:", schwarz, " Weiss: ", weiss)
        if schwarz == Global.Chois:
            print(Colorize("YOU WON!", "G"))
            return
        if i == Global.ATTEMPTS:
            print(Colorize("YOU LOSE", "R"))
            return


def Stew(text: str) -> int:
    length = len(text)
    return 61 - (length / 2)
