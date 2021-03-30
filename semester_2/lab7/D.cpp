#include <iostream>

using namespace std;

struct Man
{
    string name;
    short int status;
    bool info;
};


int main(){
    int N, days;
    bool info;
    cin >> N;
    cin >> info;

    Man* people = new Man[N]{};
    for (int i = 0; i < N; i++){
        cin >> people[i].name;
        cin >> people[i].status;
    }
    people[0].info = info;

    cin >> days;

    for (int i = 1; i <= days; i++){
        if (people[i-1].status == 0){
            people[i].info = !(people[i-1].info);
            if (people[i].info)
                people[i-1].status = 1;
        } else {
            people[i].info = people[i-1].info;
            if (people[i-1].info == 0)
                people[i-1].status = -1;
        }

    }

    for (int i = 0; i < N; i++){
        if (people[i].status != -1)
            cout << people[i].name << " " << people[i].status << endl;
    }

    
    delete [] people;
    return 0;
}