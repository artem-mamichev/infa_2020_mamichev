#include <iostream>

using namespace std;

struct Node { 
    int value;
    Node * next = NULL;
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
        new_node->value = value;
        tail = new_node;
        ++size;
    }
};


struct HashMap
{
    int length = 10;
    int elements_number = 0;
    List* arr = new List[length]{};

    int hash(int key)
    {
        return (key * (length - 1)) % length;
    }

    void realloc()
    {
        List* new_arr = new List[length * 2]{};
        for (int i = 0; i < length; i++){
            new_arr[i] = arr[i];
            arr[i].clear();
        }
        delete [] arr;
        arr = new_arr;
        length *= 2;
    }

    void add(int key)
    {
        elements_number += 1;
        if ((float) length / elements_number < 2)
            realloc();
        arr[hash(key)].push_back(key);
    }

    Node* get(int key)
    {
        if (arr[hash(key)].head == NULL)
            return NULL;
        else{
            Node* temp = arr[hash(key)].head;
            while(temp -> value != key)
            {
                temp = temp -> next;
            }
            return temp;
        }
    }

    void pop(int key)
    {
        List list = arr[hash(key)];
        if (list.size < 2)
            list.clear();
        else{
            bool exists = true;
            Node* temp = list.head;                          
            while(temp -> next -> value != key && exists)
            {
                temp = temp -> next;
                if (temp -> next == NULL)
                    exists = false;
            }
            if (exists)
            {
                delete temp -> next;
                temp -> next = temp -> next -> next;
            }
        }
    }


};

int main()
{
    
}