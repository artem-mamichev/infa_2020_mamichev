#include <iostream>
// #include <bits/stdc++.h>

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
    
    void pop()
    {
        if (size == 1){
            clear();
        }
        else{
        tail = tail -> prev;
        size--;
        }
    }

};


int main()
{
    int a;
    List * list = new List;

    std::cin >> a;
    while (a != 0){
        if (a > 0)
            list -> push_back(a);
        else {
            if (-a < list->tail->value)
                list -> tail -> value += a;
            else if (list -> size > 0)
                list -> pop();
        }
        std::cin >> a;
    }
    
    std::cout << list -> size << ' ';
    if (list -> size == 0)
        std:: cout << -1 << '\n';
    else
        std:: cout << list -> tail -> value << '\n';
    
    list->clear();
    delete list;
    return 0;
}
