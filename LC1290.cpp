/*
Title       : 1290. Convert Binary Number in a Linked List to Integer
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 3 Oct 2023
Solved Using    : CPP
*/

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        ListNode* p=head;
        int res=0;
        while(p){
           res=res*2 + p->val;
            p=p->next;
        }
        return res;
    }
};

// Time Complexity: O(n)
// Space Complexity: O(1)
// 0ms, 8.6mb

/*
The code above is a C++ implementation of a solution to the 
LeetCode problem 1290. The problem asks us to convert a 
binary number represented as a linked list to an integer.

The code defines a struct ListNode which represents a node in 
the linked list. Each node has an integer value and a pointer 
to the next node. The Solution class contains a single public 
method getDecimalValue which takes a pointer to the head of 
the linked list as input and returns an integer.

The getDecimalValue method initializes a pointer p to the head 
of the linked list and an integer res to 0. It then enters a 
while loop which continues as long as p is not null. Inside 
the loop, it multiplies res by 2 and adds the value of the 
current node p->val. It then updates p to point to the next 
node in the linked list. Finally, it returns the integer res.

The code is a straightforward implementation of the problem 
statement. It traverses the linked list once and performs a 
constant amount of work for each node. Therefore, the time 
complexity of the code is O(n), where n is the number of 
nodes in the linked list. The space complexity of the code 
is O(1), because it only uses a constant amount of extra 
space to store the integer result and the pointer to the 
current node.
*/