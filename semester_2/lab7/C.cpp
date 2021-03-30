#include <iostream>
#include <cmath>
#include <iomanip> 

using namespace std;

int arr[100000]{};

int main(){
    float a = 1, M, D, sum = 0, sum_square = 0;
    int N = 0;

    cin >> a;
    while (a != 0){
        arr[N] = a;
        N++;
        cin >> a;
    }
    
    for (int i = 0; i < N; i++){
        sum += arr[i];
        sum_square += pow(arr[i], 2);
    }
    M = sum / N;
    D = sum_square / N - pow(M, 2);

    cout << fixed << setprecision(3) << M << ' ' << D << '\n';
    return 0;
}