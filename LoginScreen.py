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


def mainMenu():
    print(f"{'':<45}  Choose what you want [1 - 3]\n")
    print(f"{'':<45}[1] Play with 4 Pin and 6 Color.")
    print(f"{'':<45}[2] Play with 6 Pin and 8 Color.")
    print(f"\n{'':<45}[0] To Exit.")


drawScreenHeader("MisterMind")
mainMenu()
