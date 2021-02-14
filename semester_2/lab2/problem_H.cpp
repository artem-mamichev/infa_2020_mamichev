#include <iostream>
#include <cmath>

using namespace std;

bool is_prime(int a){
    if (a == 2)
        return 1;
    else
        for(int i=2; i<=sqrt(a) + 1; i++)
            if (a % i == 0)
                return 0;
    
    return 1;  
}

int main(){
    int a;
    cin >> a;
    
    for (int i=2; a!=1; i++){
        if (is_prime(i))
            while (a % i == 0){
                a /= i;
                cout << i << endl;
            }
    }

    return 0;
}