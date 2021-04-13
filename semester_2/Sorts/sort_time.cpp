#include <iostream>
#include <random>
#include <chrono>
#include <vector>

using namespace std;

void bubble_sort(int* m, int n)
{
    bool sorted = false;
    int count = 0;
    while (!sorted)
    {
        sorted = true;
        for (int i = 0; i < n - 1; i++)
            if (m[i] > m[i + 1])
            {
                std::swap(m[i], m[i + 1]);
                sorted = false;
                count++;
            }k

    }
}

void selection_sort(int* m, int n)
{
    for (int i = n - 1; i > 0; i--)
    {
        int maxx = 0;
        for (int j = 1; j <= i; j++)
            if (m[j] > m[maxx]) maxx = j;
        std::swap(m[i], m[maxx]);
    }
}

void insertion_sort(int* m, int n)
{
    for (int i = 1; i < n; i++)
    {
        int etalon = m[i], j = i - 1;
        while (j >= 0 && m[j] > etalon)
        {
            m[j + 1] = m[j];
            j--;
        }
        m[j + 1] = etalon;
    }
}

void mergesort(int* m, int st, int fin)
{
    int* c = new int[fin - st + 1];
    int mid = (st + fin) / 2;
    if (st < mid) mergesort(m, st, mid);
    if (mid + 1 < fin) mergesort(m, mid + 1, fin);
    int i = st;
    int j = mid + 1;
    int p = 0;
    while (i <= mid && j <= fin)
    {
        if (m[i] <= m[j])
        {
            c[p] = m[i];
            p++;
            i++;
        }
        else
        {
            c[p] = m[j];
            p++;
            j++;
        }
    }
    while (i <= mid)
    {
        c[p] = m[i];
        p++;
        i++;
    }
    while (j <= fin)
    {
        c[p] = m[j];
        p++;
        j++;
    }
    for (int i = st; i <= fin; i++)
    {
        m[i] = c[i - st];
    }
}


struct EasySort{
    function<void(int*, int)> func;
    string name;
};


int main(){
    std::mt19937 engine(23);
    std::uniform_int_distribution<int> int_dist(0, 1000);

    EasySort bubble {bubble_sort, "Bubble"}, 
         selection {selection_sort, "Selection"},
         insertion {insertion_sort, "Insertion"};

    EasySort list_of_sorts[3] {bubble, selection, insertion};

    const int base = 1000;  // min number of elements
    const int measures_number = 5;
    int mass[base * 10]{};

     // easy sorts
    for (EasySort sort : list_of_sorts){
        cout << endl;
        cout << sort.name << endl;
        float sum_time = 0;
        for (int factor = 1; factor <= 10; factor++){
            for (int j = 0; j < measures_number; j++){  // trying with 5 different distributions
                for (int i = 1; i < base * factor; i++)
                    mass[i] = int_dist(engine);
                auto start = chrono::high_resolution_clock::now();
                sort.func(mass, base * factor);
                auto end = chrono::high_resolution_clock::now();
                auto time = end - start;
                sum_time += (float)time.count() / 1000000;
            }
            //cout << "N: " << factor << " * 10^3     " << "time: " << sum_time / measures_number << " ms" << endl;
            cout << sum_time / measures_number << ", ";
        }
    }

    //mergesort
    cout << endl;
    cout << "Merge sort" << endl;
    float sum_time = 0;
    for (int factor = 1; factor <= 10; factor++){
        for (int j = 0; j < measures_number; j++){  // trying with 5 different distributions
            for (int i = 1; i < base * factor; i++)
                mass[i] = int_dist(engine);
            auto start = chrono::high_resolution_clock::now();
            mergesort(mass, 0, factor * base - 1);
            auto end = chrono::high_resolution_clock::now();
            auto time = end - start;
            sum_time += (float)time.count() / 1000000;
        }
        //cout << "N: " << factor << " * 10^3     " << "time: " << sum_time / measures_number << " ms" << endl;
        cout << sum_time / measures_number << ", ";
    }
    cout << endl << endl;;

    //Already sorted

    // easy sorts
    cout << "Already sorted case" << endl;
    for (EasySort sort : list_of_sorts){
        cout << endl;
        cout << sort.name << endl;
        float sum_time = 0;
        for (int factor = 1; factor <= 10; factor++){
            for (int i = 1; i < base * factor; i++)
                mass[i] = i;
            auto start = chrono::high_resolution_clock::now();
            sort.func(mass, base * factor);
            auto end = chrono::high_resolution_clock::now();
            auto time = end - start;
            sum_time += (float)time.count() / 1000000;
            //cout << "N: " << factor << " * 10^3     " << "time: " << sum_time / measures_number << " ms" << endl;
            cout << sum_time / measures_number << ", ";
        }
    }

    //mergesort
    cout << endl;
    cout << "Merge sort" << endl;
    sum_time = 0;
    for (int factor = 1; factor <= 10; factor++){
        for (int i = 1; i < factor * base; i++)
            mass[i] = i;
        auto start = chrono::high_resolution_clock::now();
        mergesort(mass, 0, factor * base - 1);
        auto end = chrono::high_resolution_clock::now();
        auto time = end - start;
        sum_time += (float)time.count() / 1000000;
    
        //cout << "N: " << factor << " * 10^3     " << "time: " << sum_time / measures_number << " ms" << endl;
        cout << sum_time / measures_number << ", ";
    }
    cout << endl;
    return 0;
}
