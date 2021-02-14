#include <iostream>

using namespace std;

int main(){
    int a; int counter = 0;

    while ((cin >> a) && a != 0)
        if (a % 2 == 0)
            counter++;

    cout << counter << endl;

    return 0;
}