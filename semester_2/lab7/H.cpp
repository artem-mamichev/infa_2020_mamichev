#include <iostream>

using namespace std;

int main(){
    int i = 0, j = 0;
    int N, min;
    cin >> N;
    bool found = false;

    int* arr = new int[N];

    for(int i = 0; i < N; i++){
        cin >> arr[i];
    }
    while (i < N - 1){
        while (!(arr[i] < 0) && i < N)
            i++;
        if (i != N){
            j = i;
            while (!(arr[j] > 0 && arr[j] == -arr[i]) && j < N)
                j++;
            if (!(j == N)){
                if (j - i < min || !found)
                    min = j - i;
                found = true;
            }
            i++;
        }
    }

    if (!found)
        cout << 0;
    else
        cout << min;
    
    return 0;
}