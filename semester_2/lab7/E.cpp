#include <iostream>

using std:: cin;
using std:: cout;

int arr[1000][1000];

int main(){
    int N;
    cin >> N;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> arr[j][N - i - 1];

    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++)
            cout << arr[i][j] << ' ';
        cout << '\n';
    }

    return 0;
}