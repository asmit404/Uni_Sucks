"""
Title       : 2. Add Two Numbers
Difficulty  : Medium
Author      : Asmit Singh
Solved On   : 31 Dec 2023
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode()
        carry = 0
        while l1 or l2 or carry:
            carry, out = divmod((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry, 10)
            curr.next = curr = ListNode(out)
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return dummy.next

# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n))