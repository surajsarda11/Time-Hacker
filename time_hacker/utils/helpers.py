def print_colored(text, color="cyan"):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "cyan": "\033[96m",
        "end": "\033[0m"
    }
    print(f"{colors.get(color, '')}{text}{colors['end']}")
