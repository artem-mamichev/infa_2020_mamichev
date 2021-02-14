#include <iostream>
#include <string>

using namespace std;


void parse_input(string str, int* v, string* car_code){
    int i = 0;
    *v = 0;
    while (str[i] != ' '){
        *v = *v * 10 + int(str[i]) - 48;
        i++;
    }
    *car_code = str.substr(i + 1, 6);
}


int fine(string car_code){
    int number_same = 1, fine = 0;
    string car_numbers = car_code.substr(1, 3);

    for (int i=0; i<=1; i++)
        for (int j=i+1; j<=2; j++)
            if (car_numbers[i]==car_numbers[j] && number_same<3)
                number_same++;

    switch (number_same){
    case 4: 
        fine = 20000;
        break;
    case 3: 
        fine = 1000;
        break;
    case 2: 
        fine = 500;
        break;
    case 1: 
        fine = 100;
        break;
    }
    return fine;
}


int main(){
    string str, car_code; 
    int v = 0, res = 0;

    while (car_code != "A999AA"){
        if (v > 60)
            res += fine(car_code);
        getline(cin, str);
        parse_input(str, &v, &car_code);
    }
    
    cout << res << endl;
    return 0;
}