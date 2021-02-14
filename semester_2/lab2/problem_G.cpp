#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int a){
    for(int i=2; i<=sqrt(a) + 1; i++)
        if (a % i == 0)
            return 0;
    
    return 1;  
}

int main(){
    int a;
    cin >> a;
    
    cout << is_prime(a) << endl;

    return 0;
}