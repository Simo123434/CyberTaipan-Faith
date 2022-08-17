# Imports
import os

# Check that script running as root
def check_root():
    if os.getuid() != 0:
        print("Please run as root and try again.")
        exit(1)
    else:
        print("Running as root \nStarting checks")

# Run update to ensure everything is updated
def update():
    print("Performing system update")
    os.system("sudo apt-get update > /dev/null && sudo apt-get upgrade -y > /dev/null")


# check if firewall is installed and if not install it and turn it on
def ufw_check():
    print("Checking if the firewall is enabled")
    if os.system("sudo ufw status").read() == 'Status: inactive':
        os.system("sudo ufw enable > /dev/null")
        print("Firewall started")
    else:
        print("Firewall already active")
        
def unauthorised_files():
    print("Removing unauthorised files")
    disallowedExt = input("What are the disallowed file extensions? (seperate by comma e.g. mp3,mp4)\nfile extension: ") # get user input for files not allowed according to readme from the box
    notallowedExt = []
    notallowedExt = disallowedExt.split(",") # split the input by comma and add it to the array
    for i in notallowedExt:
        print("The disallowed files with the extension " + i + " are: \n")
        os.system("sudo find / -name *." + i + " 2>/dev/null") # find files with extension and send errors to null
        
    
def checkUsers():
    print("Listing all users, please check readme to see which users are not allowed\n")
    os.system("sudo getent passwd |cut -d: -f1")
    


# Main Function
def main():
    check_root()
    update()
    ufw_check()
    unauthorised_files()
    checkUsers()
    


if __name__ == "__main__":
    main()