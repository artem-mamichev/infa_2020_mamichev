#include <iostream>

using namespace std;

struct item
{
    string FIO;
    long long num;
    long long balance;
};

void selection_sort(item* m, int N)
{
    for (int i = N - 1; i > 0; i--)
    {
        int maxx = 0;
        for (int j = 1; j <= i; j++)
            if (m[j].balance > m[maxx].balance) maxx = j;
        std::swap(m[i], m[maxx]);
    }
}
    
int main(){
    int N;
    cin >> N;

    item* data = new item[N];
    for (int i = 0; i < N; i++){
        cin >> data[i].FIO >> data[i].num >> data[i].balance;
    }
    
    selection_sort(data, N);

    if (N <= 100)
        for (int i = 0; i < N; i++){
            if (data[i].balance < 0)
                cout << data[i].FIO << " " << data[i].num << " " << data[i].balance << endl;
        }
    else
        for (int i = 0; i < N; i++)
            if (data[i].balance < 0)
                cout << data[i].FIO << " " << data[i].num << " " << data[i].balance << endl;

    delete [] data;
    return 0;
}