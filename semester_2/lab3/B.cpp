#include <iostream>

using namespace std;


int main(){
    long int n, k;
    int m; 

    cin >> n;
    cin >> m;
    cin >> k;   

    int **polygon = new int *[n];
    for (int i = 0; i < n; i++){
        polygon[i] = new int[m]{};
    }

    for (int count = 1; count <= 2*k; count+=2){
        long int bomb_i; 
        int bomb_j;
        cin >> bomb_i;
        cin >> bomb_j;
        polygon[bomb_i-1][bomb_j-1] = -1;
        for (int i=bomb_i-2; i<=bomb_i; i++){
            for (int j=bomb_j-2; j<=bomb_j; j++){
                if (i >= 0 && i < n && j >= 0 && j < m && !(polygon[i][j] == -1))
                    polygon[i][j] += 1;
            }
        }
    }

    for (int i=0; i<n; i++){
        for (int j=0; j<m; j++)
            cout << polygon[i][j] << " ";
        cout << endl;
    }

    for (int i=0; i<n; i++)
        delete [] polygon[i];
    delete [] polygon;

    return 0;
}