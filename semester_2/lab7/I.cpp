#include <iostream>
#include <algorithm>

using namespace std;


bool key(int a, int b){
    bool flag;
    if ((a % 2 == 0 && b % 2 == 0) || (a % 2 != 0 && b % 2 != 0))
        flag = a < b;
    if (a % 2 == 0 && b % 2 != 0)
        flag = true;
    if (a % 2 != 0 && b % 2 == 0)
        flag = false;
    return flag;
}

int main(){
    int arr[10000];
    int a, i = 0;

    while (cin >> a){
        arr[i] = a;
        i++;
    }
    sort(arr, arr + i, key);

    for (int j = 0; j < 7; j++)
        cout << arr[j] << ' ';
    return 0;
}