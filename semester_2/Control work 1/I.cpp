#include <iostream>

using namespace std;


void selection_sort(long int* m1, long int* m2, int n)
{
    for (int i = n - 1; i > 0; i--)
    {
        int maxx = 0;
        for (int j = 1; j <= i; j++)
            if ((m1[j] > m1[maxx]) || (m1[j] == m1[maxx] && m2[j] > m2[maxx])) maxx = j;
        swap(m1[i], m1[maxx]);
        swap(m2[i], m2[maxx]);
    }
}


int main(){
    int N;
    long int num;
    cin >> N;

    long int* arr1 = new long int[N];
    long int* arr2 = new long int[N];

    for(int j = 0; j < N; j++)
        cin >> arr1[j];
    for(int j = 0; j < N; j++)
        cin >> arr2[j];
    
    selection_sort(arr1, arr2, N);

    for(int j = 0; j < N; j++)
        cout << arr1[j] << " ";
    cout << endl;
    for(int j = 0; j < N; j++)
        cout << arr2[j] << " ";

    delete [] arr1;
    delete [] arr2;

    return 0;
}