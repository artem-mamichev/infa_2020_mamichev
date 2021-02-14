#include <iostream>
#include <string>
#include <cmath>

using namespace std;


string babylonian (int num){
    string str = "";
    int power = 0;
    while (pow(60, power) <= num){
        power++;
    }
    power--;
    
    while (power >= 0){
        int val = num / (int)pow(60, power);

        string str_val = string(val / 10, '<') + string(val % 10, 'v');
        str += str_val + ".";

        num -= val * pow(60, power);
        power--;
    }
    str.erase(str.size() - 1);  // delete last "."

    return str;
}


int main(){
    long int num;
    cin >> num;

    cout << babylonian(num) << endl;
    return 0;
}