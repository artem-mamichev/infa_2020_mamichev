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

    void push_middle(int value)
    {
        if (head == NULL) {
            head = new Node;
            head->value = value;
            tail = head;
            size = 1;
            return;
        }
        if (size == 1)  // Почему при size == 1 new_node = head -> next выбрасывает ошибку???
            push_back(value);
        else{
            int position = size % 2 == 0 ? (size / 2) + 1 : (size / 2 + 2);  // head - first in queue
        
            Node* temp = head;
            for (int i = 1; i < position - 1; i++){
                temp = temp -> next;
            }
            Node* new_node = new Node;
            new_node -> value = value;
            new_node -> next = temp -> next; 
            //temp -> next -> prev = new_node;
            temp -> next = new_node;
            //new_node -> prev = temp;
            size++;
        }
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
            size--;
        }
        return value;
    }

    int pop_head()
    {
        int value = 0;
        if (head != NULL)
            value = head -> value;
            Node * old_head = head;
            head = head -> next;
            delete old_head;
            size--;
        return value;
    }

};


int main()
{
    char sign;
    int N, number;
    cin >> N;

    List* list = new List;

    for (int i = 0; i < N; i++){
        cin >> sign;
        if (sign == '-')
            cout << list -> pop_head() << endl;
        else{
            cin >> number;
            if (sign == '+')
                list -> push_back(number);
            else if (sign == '*')
                list -> push_middle(number);
        }
    }

    list -> clear();
    delete list;
    return 0;
}
