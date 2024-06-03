// main.cpp
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {
    int number = 5;
    string command = "python script.py " + to_string(number);
    system(command.c_str());
    return 0;
}
