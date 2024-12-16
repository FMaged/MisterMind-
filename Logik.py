import os
import random
import sys

import Global
import LoginScreen
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


def Colorized_list(list: list) -> str:
    Colorized_list = []
    for char in list:
        Colorized_list.append(Colorize(char, char))
    return "".join(Colorized_list)


def generate_Secrate_Code(Colors: list, code_Lenght: int) -> list:
    printt(f"DEBUG: Generating secret code .... {Colorized_list(Colors)}")
    return random.choices(Global.COLORS, k=Global.Chois)


def CalculateMatches(Secret_Code: list, GuessList: list) -> tuple:
    schwarz = 0
    weiss = 0
    for i in range(len(Secret_Code)):
        if GuessList[i] == Secret_Code[i]:
            schwarz += 1
        Set_GuessList = set(GuessList)
        if Secret_Code[i] in Set_GuessList:
            weiss += 1
    return schwarz, (weiss - schwarz)


def play_Game() -> None:
    LoginScreen.drawScreenHeader("MisterMind")
    secret_Code = generate_Secrate_Code(Global.COLORS, Global.Chois)
    printt(f" DEBUG: Secret Code: {Colorized_list(secret_Code)}")
    for i in range(Global.ATTEMPTS):
        GuessList = validate.readSpecificChars(secret_Code, Global.Chois, "Enter your guess: ")
        sys.stdout.write("\033[F")  # Move the cursor up one line
        sys.stdout.write("\033[K")  # Clear the line
        schwarz, weiss = CalculateMatches(secret_Code, GuessList)
        Colorized_list_Str = Colorized_list(GuessList)
        printt(f"Attempt {i + 1} {Colorized_list_Str} schwarz: {schwarz}, Weiss:  {weiss}")
        if schwarz == Global.Chois:
            printt(f"{Colorize("     YOU WON!", "G")}")
            return
        if i >= Global.ATTEMPTS - 1:
            printt(f"{Colorize("     YOU LOSE!", "R")}")
            return


def printt(text: str) -> int:
    length = len(text)
    stew = 61 - (length / 5)
    print(f"{'':<{stew}}{text}")
