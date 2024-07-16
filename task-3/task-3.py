import sys
from pathlib import Path
from colorama import Fore, Style


def visualize_directory_structure(directory_path, depth=0):
    try:
        directory = Path(directory_path)
        if not directory.is_dir():
            print(f"{Fore.RED}Error: {directory_path} is not a directory.{Style.RESET_ALL}")
            return

        if depth == 0:
            print(f"{Fore.BLUE}{'   ' * depth}{directory.name}/{Style.RESET_ALL}")  # Print root folder

        for item in directory.iterdir():
            if item.is_dir():
                print(f"{Fore.BLUE}{'   ' * (depth + 1)}{item.name}/{Style.RESET_ALL}")
                visualize_directory_structure(item, depth + 2)
            else:
                print(f"{Fore.GREEN}{'   ' * (depth + 1)}{item.name}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}Error during processing folder: {e}{Style.RESET_ALL}")


if len(sys.argv) != 2:
    print(f"{Fore.RED}Usage: python script.py /path/to/directory{Style.RESET_ALL}")
else:
    directory_path = sys.argv[1]
    visualize_directory_structure(directory_path)
