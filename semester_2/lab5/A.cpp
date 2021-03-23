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
            Node * old_tail = tail;
            tail = tail -> prev;
            delete old_tail;
            tail -> next = NULL;
            size--;
        }
        return value;
    }

};


int main()
{
    int a;
    List * list = new List;

    cin >> a;
    while (a != 0){
        if (a > 0)
            list -> push_back(a);
        else if (list -> size > 0){
                if (-a < list -> tail -> value)
                    list -> tail -> value += a;
                else 
                    list -> pop();
        }
        cin >> a;
    }
    
    cout << list -> size << ' ';
    if (list -> size == 0)
        cout << -1 << '\n';
    else
        cout << list -> tail -> value << '\n';
    
    list->clear();
    delete list;
    return 0;
}
