#include <iostream>
#include <fstream>

using namespace std;

void writeLineToFile(string line, string fileName) {
    // Open the file for writing
    ofstream outputFile(fileName, ios::out | ios::app);

    if (outputFile.is_open()) {
        // Write the line to the file
        outputFile << line << endl;

        // Close the file
        outputFile.close();

        cout << "Line written to file successfully." << endl;

        // Open the file for reading
        ifstream inputFile(fileName);

        if (inputFile.is_open()) {
            string fileContent;
            // Read the file contents and print them to the console
            while (getline(inputFile, fileContent)) {
                cout << fileContent << endl;
            }

            // Close the file
            inputFile.close();
        } else {
            cout << "Error: Unable to open file for reading." << endl;
        }
    } else {
        cout << "Error: Unable to open file for writing." << endl;
    }
}

int main() {
    string line = "This is the line I want to write to the file.";
    string fileName = "example.txt";

    writeLineToFile(line, fileName);
    return 0;
}
