import os

# LIST OF APPS TO BE INSTALLED
APPS = ["vlc","git","telegram-desktop","spotify-client","qbittorrent"]

def install_apps_ubuntu():
    os.system("sudo apt update")
    for app in APPS:
        choice = input(f"Do you want to install {app}? (y/n): ").strip().lower()
        if choice == 'y':
            os.system(f"sudo apt install -y {app}")
        else:
            print(f"Skipping {app}")

def install_apps_fedora():
    for app in APPS:
        choice = input(f"Do you want to install {app}? (y/n): ").strip().lower()
        if choice == 'y':
            os.system(f"sudo dnf install -y {app}")
        else:
            print(f"Skipping {app}")

def install_apps_arch():
    for app in APPS:
        choice = input(f"Do you want to install {app}? (y/n): ").strip().lower()
        if choice == 'y':
            os.system(f"sudo pacman -Sy {app}")
        else:
            print(f"Skipping {app}")

def main():
    print("Which Linux distribution are you using?")
    print("1. Ubuntu & derivatives")
    print("2. Fedora")
    print("3. Arch")
    distro = input("Choose your distribution(1-3)").strip()

    if distro == '1':
        install_apps_ubuntu()
    elif distro == '2':
        install_apps_fedora()
    elif distro == '3':
        install_apps_arch()
    else:
        print("Invalid option. Please run the script again and choose a valid option.")
        exit(1)

    print("Installation process complete.")

if __name__ == "__main__":
    main()
