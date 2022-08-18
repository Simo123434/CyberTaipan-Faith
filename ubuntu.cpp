#include <iostream>
#include <unistd.h>

using namespace std;

int getPriv() {
    auto currPrivs = geteuid(); // Get current uid

    if (currPrivs != 0) {
        cout << "Not running as root, try again with root privelages!" << endl;
        return 0;
    } 
    else {
        cout << "You are root, beginning script!" << endl;
        return 1;
    }
}


int main() {

    // Check if script is running as root
    if (getPriv() == 1) {
        
        return 0;
    }
    else {
        return 1;
    }

}