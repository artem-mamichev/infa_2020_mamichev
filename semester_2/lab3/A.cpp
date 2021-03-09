#include <iostream>

using namespace std;


int main(){
    int sum = 0;
    float average;
    int n, a;
    cin >> n;

    int * arr = new int[n];
    for(int i=0; i<n; i++){
        cin >> a;
        arr[i] = a;
        sum += a;
    }

    average = (float)sum / n;
    sum = 0;

    for(int i=0; i<n; i++){
        if (arr[i] > average)
            sum += arr[i];
    }

    cout << sum << endl;
    delete [] arr;

    return 0;
}