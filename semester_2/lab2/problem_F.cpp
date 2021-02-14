#include <iostream>

using namespace std;

int main(){
    int a, max = 0, counter = 0;

    while ((cin >> a) && a != 0){
        if (a > max){
            max = a;
            counter = 0;
        }
        if (a == max)
            counter++;
    }
    
    cout << counter << endl;

    return 0;
}