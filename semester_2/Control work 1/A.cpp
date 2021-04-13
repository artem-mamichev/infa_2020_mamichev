#include <iostream>

using namespace std;


int sum_num(int n){
    int res = 0;
    for (int i = 0; i < 3; i++){
        res += n % 10;
        n /= 10;
    }
    return res;
}


int main(){
    int n;
    cin >> n;
    cout << sum_num(n) << endl;
    return 0;
}