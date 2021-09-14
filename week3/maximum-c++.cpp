

// If first number1 >= number2 then
//     Display number1
// Else
//     Display number2
// End if

#include <iostream>

using namespace std;

int main()
{
    // Display “Enter a first number”
    // Create variable number1 and read input to it
    // Display “Enter a first number”
    // Create variable number2 and read input to it
    
    int number1, number2;
    cout << "Enter a first number" << endl;
    cin >> number1;

    cout << "Enter a second number" << endl;
    cin >> number2;

    // If first number1 >= number2 then
    //     Display number1
    // Else
    //     Display number2
    // End if

    if(number1 >= number2)
    {
        cout << number1 << " is the largest " << endl;
    }
    else
    {
        cout << number2 << " is the largest " << endl;
    }

    return 0;
}