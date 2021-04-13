#include <iostream>

using namespace std;


int main(){
    long int N;
    double M, F;
    cin >> N;

    for(int i = 0; i < N; i++){
        M = 0.3*(100 + 2*F) + 10;
        F = 0.7*(100 + 2*F);
    }
    cout << static_cast<int64_t>(M);
    return 0;
}