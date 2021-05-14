#include <iostream>
#include <algorithm>

using namespace std;

struct item
{
    string FIO;
    long long num;
    long long balance;
};

int main()
{
    int n;
    cin >> n;

    item* data = new item[n];
    for (int i = 0; i < n; i++)
        cin >> data[i].FIO >> data[i].num >> data[i].balance;

    sort(data, data + n, [](item a, item b) -> bool {
        if (a.balance > b.balance)
            return true;
        if (a.balance < b.balance) 
            return false;
        if (a.FIO < b.FIO) 
            return true;
        if (a.FIO > b.FIO) 
            return false;
        if (a.num < b.num) 
            return true;
        return false;
    });

    if (n <= 10)
        for (int i = 0; i < n; i++)
            cout << data[i].FIO << ' ' << data[i].num << ' ' << data[i].balance << endl;
    else
        for (int i = 0; i < 10; i++) 
            cout << data[i].FIO << ' ' << data[i].num << ' ' << data[i].balance << endl;

    delete [] data;
    return 0;
}