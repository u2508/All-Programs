#include<iostream>
using namespace std;
int main()
{int arr[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}},*ptr;

// Assign the address of the first element to the pointer
ptr = &arr[0][0];

// Access the elements of the array using pointer arithmetic
for (int i = 0; i < 9; i++) {
    for (int j = 0; j < 3; j++) {
        // Access the element at row i, column j
        int element = *(ptr++);
        // Do something with the element
        // ...
        cout<<element<<"\t";
    }
    cout<<"\n";
}
return 0;
}