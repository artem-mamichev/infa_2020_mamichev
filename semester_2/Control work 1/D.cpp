#include <iostream>

using namespace std;


int main(){
    int max = 0;
    int current = 0;
    string str;
    getline(cin, str);
    for (char a : str){
        if ((int)a > 47 && (int)a < 58)
            current = current * 10 + int(a) - 48;
        else{
            if (current > max)
                max = current;
            current = 0;
        }
    }
    if (current > max)
        max = current;
     
    cout << max;
    return 0;
}