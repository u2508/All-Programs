#include <iostream>
#include <string>
using namespace std;
void riskyFunction() {
    // Simulating an error condition
    bool error = true;
    if (error) {
        throw runtime_error("An error occurred!"); // Throwing an exception
    }
}

int main() {
    try {
        std::cout << "Starting try block..." << std::endl;
        riskyFunction(); // Calling the risky function
        std::cout << "Exiting try block normally." << std::endl;
    } catch (const std::exception& e) { // Catching the exception
        std::cerr << "Caught an exception: " << e.what() << std::endl;
    } // C++ does not have a "finally" block like some other languages, so this is just a comment
    std::cout << "Inside finally block (just a comment)." << std::endl;
    

    std::cout << "Program continues normally after exception handling." << std::endl;

    return 0;
}
