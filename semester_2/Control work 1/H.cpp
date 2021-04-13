#include <iostream>

using namespace std;


int main(){
    int N, K;
    int num;
    int position = 1;
    bool found = false;

    cin >> N >> K;
    
    cin >> num;
    while (!found && position < N){
        cin >> num;
        if (num == K)
            found = true;
        position++;
    }
    if (!found)
        cout << -1 << endl;
    else
        cout << position << endl;

    return 0;
}