/*
Title       : 234. Palindrome Linked List
Difficulty  : Easy
Author      : Asmit Singh
Solved On   : 3 Oct 2023
Solved Using    : CPP
*/

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    bool isPalindrome(ListNode *head)
    {
        int n = 0;
        ListNode *p = head;
        ListNode *p1;
        ListNode *new_head = new ListNode(0);
        while (p)
        {
            n++;
            p = p->next;
        }
        p = head;
        for (int i = 0; i < n / 2; i++)
        {
            ListNode *t = new_head->next;
            new_head->next = p;
            p = p->next;
            new_head->next->next = t;
        }
        if (n % 2 == 1)
        {
            p = p->next;
        }
        p1 = new_head->next;
        while (p)
        {
            if (p->val != p1->val)
                return false;
            p = p->next;
            p1 = p1->next;
        }
        return true;
    }
};

// Time Complexity: O(n)
// Space Complexity: O(1)
// 127ms, 110.78mb

/*
The code above is an implementation of the LeetCode problem 234.
The problem asks us to determine whether a given singly linked list
is a palindrome. A palindrome is a sequence of characters that reads
the same backward as forward. The code starts by finding the length
of the linked list by traversing it once. It then uses this length
to split the linked list into two halves. The first half is reversed
by iterating over it and changing the pointers to reverse the order
of the nodes. If the length of the linked list is odd, we skip the
middle node by moving the pointer to the next node. We then compare
the values of the nodes in the first half of the linked list with
the second half of the linked list. If any of the values do not match,
we return false. If all the values match, we return true.
*/