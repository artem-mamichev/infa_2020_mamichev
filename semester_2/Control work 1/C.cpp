#include <iostream>

using namespace std;


int main(){
string str;
int counter = 0;
getline(cin, str);
for (char letter : str){
    if (letter == ' ')
        cout << ' ';
    else{
        if (counter % 2 == 0 && ((int)letter - 32) > 64)
            cout << (char)((int)letter - 32);
        else if (counter % 2 == 1 && (int)letter + 32 < 123)
            cout << (char)((int)letter + 32);
        else
            cout << letter;
        counter++;
    }
}

return 0;
}