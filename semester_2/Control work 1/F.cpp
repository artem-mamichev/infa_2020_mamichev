#include <iostream>

using namespace std;


long int tribo(int n){
    int temp;
    long int t0 = 0, t1 = 0, t2 = 1;
    if (n == 0 || n == 1)
        return 0;
    if (n == 2)
        return 1;
    for(int i = 0; i < n - 2; i++){
        temp = t2;
        t2 = t0 + t1 + t2;
        t0 = t1;
        t1 = temp;
    }
    return t2;
}


int main(){
    long int num;
    int i = 0;
    cin >> num;
    while (tribo(i) <= num)
        i++;
    cout << i << endl;
    return 0;
}