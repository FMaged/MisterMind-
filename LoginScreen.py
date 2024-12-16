import Global
import Logik
import validate

ScreenOptions: dict = {
    1: "4Pins",
    2: "6Pins",
    3: "Exit",
}


def drawScreenHeader(Title: str, SubTitle: str = "") -> None:
    print("\t\t\t\t\t--------------------------------------")
    print("\n\n\t\t\t\t\t\t      ", Title)
    if SubTitle != "":
        print("\n\t\t\t\t\t\t\t", SubTitle)
    print("\n\t\t\t\t\t--------------------------------------\n\n")


def mainMenu() -> None:
    print(f"{'':<45}  Choose what you want [0 - 2]\n")
    print(f"{'':<45}[1] Play with 4 Pin and 6 Color.")
    print(f"{'':<45}[2] Play with 6 Pin and 8 Color.")
    print(f"\n{'':<45}[0] To Exit.")
    chooies: int = validate.readIntBetween(0, 2)
    match chooies:
        case 1:
            Global.Chois = 4
            PinsScreen(Global.COLORS, Global.ATTEMPTS)

        case 2:
            Global.Chois = 6
            PinsScreen(Global.COLORS, Global.ATTEMPTS)

        case 3:
            pass


def PinsScreen(Colors: list, Attempts) -> None:
    validate.clear_terminal()
    drawScreenHeader("MisterMind")
    print(f"{'':<50}{Logik.Colorize("Welcome to MisterMind!", "G")}")
    print(f"{'':<42}The goal is to guess the Secret COLORE")
    print(f"{'':<36}The Code is made up of the following COLORS {Logik.Colorized_list(Colors)}")
    print(f"{'':<41}The Secret code constists of ", {Global.Chois}, " Colors")
    print(f"{'':<39}you Have {Attempts} Attempts to guess the secret code.")
    print(
        f"{'':<31}Enter your guess as a continous string of letters, e,g. '" + Logik.Colorized_list(Colors[0:4]) + "'"
    )

    input(f"{'':<48}Press Enter to continue...")

    validate.clear_terminal()
    Logik.play_Game()


def _6PinsScreen(Colors: list, Code_Length, Attempts) -> None:
    validate.clear_terminal()
    drawScreenHeader("MisterMind")
    print(f"{'':<50}{Logik.Colorize("Welcome to MisterMind!", "G")}")
    print(f"{'':<42}The goal is to guess the Secret COLORE")
    print(f"{'':<36}The Code is made up of the following COLORS {Logik.Colorized_list(Colors)}")
    print(f"{'':<41}The Secret code constists of ", {Code_Length}, " Colors")
    print(f"{'':<39}you Have {Attempts} Attempts to guess the secret code.")
    print(
        f"{'':<31}Enter your guess as a continous string of letters, e,g. '" + Logik.Colorized_list(Colors[0:4]) + "'"
    )
    input(f"{'':<48}Press Enter to continue...")
