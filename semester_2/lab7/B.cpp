#include <iostream>

using namespace std;

bool is_ok(int num){
    if (num % 4 == 0){
        if (!((num / 1000 == 4) or (num / 1000 == 5)))
            return false;
    }
    if (num % 7 == 0){
        if (!((num / 1000 == 7) or (num / 1000 == 1)))
            return false;
    }
    if (num % 9 == 0){
        if (!((num / 1000 == 8) or (num / 1000 == 9)))
            return false;
    }
    return true;
}

int main(){
    int N, num;
    bool all_ok = true;

    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> num;
        if (! is_ok(num)){
            cout << num << endl;
            all_ok = false;
        }
    }

    if (all_ok)
        cout << 0 << endl;
            
    return 0;
}