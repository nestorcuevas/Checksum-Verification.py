import hashlib
import os
from colorama import Fore, Style

# Display script description
author = "8comma1"
print(Fore.GREEN + "This script brought to you by the CodeMaster", author,
      "- It calculates the checksum of a file using different algorithms (MD5, SHA1, SHA256, SHA512)." + Style.RESET_ALL)

while True:
    # Prompt user for file path
    while True:
        file_path = input("Enter the file path: ").strip('"')
        if not os.path.exists(file_path):
            print("File path does not exist. Please enter a valid file path.")
        else:
            break

    # Prompt user for algorithm choice
    print("Choose an algorithm:")
    print("1. " + Fore.YELLOW + "MD5" + Style.RESET_ALL)
    print("2. " + Fore.CYAN + "SHA1" + Style.RESET_ALL)
    print("3. " + Fore.MAGENTA + "SHA256" + Style.RESET_ALL)
    print("4. " + Fore.GREEN + "SHA512" + Style.RESET_ALL)
    algorithm_choice = input("Enter the number corresponding to the algorithm: ")

    # Validate algorithm choice
    if algorithm_choice == "1":
        algorithm = "md5"
        algorithm_color = Fore.YELLOW
    elif algorithm_choice == "2":
        algorithm = "sha1"
        algorithm_color = Fore.CYAN
    elif algorithm_choice == "3":
        algorithm = "sha256"
        algorithm_color = Fore.MAGENTA
    elif algorithm_choice == "4":
        algorithm = "sha512"
        algorithm_color = Fore.GREEN
    else:
        print("Invalid algorithm choice. Please enter a valid number.")
        continue

    # Calculate checksum
    with open(file_path, "rb") as file:
        data = file.read()
        checksum = hashlib.new(algorithm, data).hexdigest()

    # Display the checksum with algorithm-specific color
    print("Checksum ({}):".format(algorithm), algorithm_color + checksum + Style.RESET_ALL)

    # Prompt user to check another file
    check_another_file = input("Do you want to check another file? (Y/N): ")
    if check_another_file.upper() != "Y":
        break

print(Fore.GREEN + "Go forth and do great things!" + Style.RESET_ALL)
