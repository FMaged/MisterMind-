import os
import sys


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
