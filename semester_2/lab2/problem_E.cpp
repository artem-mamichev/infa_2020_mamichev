#include <iostream>

using namespace std;

int main(){
    int max = 0; int temp; 

    while ((cin >> temp) && temp != 0)
        if (temp % 2 == 0 && temp > max)
            max = temp;

    cout << max << endl;

    return 0;
}