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
    os.system("sudo apt-get update > /dev/null && sudo apt-get upgrade -y > /dev/null")


# check if firewall is installed and if not install it and turn it on
def ufw_check():
    if os.popen("sudo ufw status").read() == 'Status: inactive':
        os.popen("sudo ufw enable")
        print("Firewall started")
    else:
        print("Firewall already active")
        
    
    

# Main Function
def main():
    print("Script started")
    check_root()
    update()


if __name__ == "__main__":
    main()