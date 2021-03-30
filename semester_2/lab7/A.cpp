#include <iostream>

using namespace std;

int main(){
    int mark = 2;
    int a, b, c, d, ans;
    cin >> a >> b >> c >> d >> ans;

    if ((a + ans == b) && (c * ans == d))
        mark = 5;
    else { if ((a + ans == b) || (c * ans == d))
               mark = 4;
           else if (ans == 1024)
               mark = 3;
    }

    cout << mark << endl;
    return 0;
}