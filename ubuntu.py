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
    if os.popen("sudo ufw status").read() == 'Status: inactive':
        os.popen("sudo ufw enable > /dev/null")
        print("Firewall started")
    else:
        print("Firewall already active")
        
def unauthorised_files(ext):
    print("Removing unautorised files")
    for i in ext:
        print(i)
        
    
    

# Main Function
def main():
    check_root()
    update()
    ufw_check()
    disallowedExt = input("What are the disallowed file extensions? (seperate by comma e.g. mp3,mp4)")
    notallowedExt = []
    notallowedExt = disallowedExt.split(",")
    unauthorised_files(notallowedExt)
    


if __name__ == "__main__":
    main()