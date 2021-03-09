#include <iostream>

using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << do_some_awesome_work(&a, &b) << endl;
    return 0;
}