#include <iostream>

using namespace std;

struct Node {
    int value;
    Node * next = NULL;
    Node * prev = NULL;
};

struct List
{
    Node * head = NULL;
    Node * tail = NULL;
    unsigned int size = 0;

    void print()
    {
        Node * p_node = head;
        while (p_node != NULL) {
            std::cout << p_node->value << ' ';
            p_node = p_node->next;
        }
        std::cout << '\n';
    }

    void clear()
    {
        while(head != NULL) {
            Node * next = head->next;
            delete head;
            head = next;
        }
        size = 0;
    }

    void push_back(int value)
    {
        if (head == NULL) {
            head = new Node;
            head->value = value;
            tail = head;
            size = 1;
            return;
        }

        Node * new_node = new Node;
        tail->next = new_node;
        new_node->prev = tail;
        new_node->value = value;
        tail = new_node;
        ++size;
    }
    
    int pop()
    {
        int value;
        if (size == 1){
            value = head -> value;
            clear();
        }
        else{
            value = tail -> value;
            tail = tail -> prev;
            size--;
        }
        return value;
    }

};


int str_to_int (string a){
    int sign = 1;
    int res = 0; 
    if (a[0] == '-'){
        sign = -1;
        a.erase(0, 1);
    }
    for (int i = a.size(); i > 0; i--){
        res += a[0] - 48;
        res *= 10;
        a.erase(0, 1);
    }
    return sign * res / 10;
}


int main()
{
    int val;
    string a;
    List * list = new List;

    while (cin >> a){
        if (a[0] == '+'){
            val = list -> pop() + list -> pop();
            list -> push_back(val);
        }
        else { if (a[0] == '*'){
                    val = list -> pop() * list -> pop();
                    list -> push_back(val);}
               else { if (a[0] == '/'){
                          val = list -> tail -> prev -> value / list -> tail -> value;
                          list -> pop();
                          list -> pop();
                          list -> push_back(val);}
                      else { if ((a[0] == '-') && (a.size() == 1)){ // отнимание, а не отрицательное число
                          val = list -> tail -> prev -> value - list -> tail -> value;
                          list -> pop();
                          list -> pop();
                          list -> push_back(val);}
                               else{
                                   list -> push_back(str_to_int(a));
                               }
                }
            }
        }
    }

    cout << list -> head -> value << endl;

    list -> clear();
    delete list;
    return 0;
}
