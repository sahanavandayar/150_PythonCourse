#include <iostream> //to use cin and cout
#include <fstream>  //to get input from a file
#include <string>   //uses strings
using namespace std;

ifstream in_file;

int main() {

    in_file.open("./p8input.txt", ios::in);
    if(in_file.fail()) {
        cout << "Could not open input file.  Program terminating.\n\n";
        return 9;
    }
    
    //Your code goes here
    //remember that you can read from the file by treating
    //  in_file like cin. For example,
    //string name;
    //in_file >> name;
    
}
