 #Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# using Recursive method , tc: o(m+n) and sc:o(m+n)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        

# using Ierative method , tc: o(m+n) and sc:o(1)
    def mergeTwoLists_Itr(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
obj = Solution()
# example usage: build two sorted lists and merge them
# list1: 0 → 1 → 2 → 3 → 4
head1 = ListNode(0)
tail = head1
for i in range(1, 5):
    tail.next = ListNode(i)
    tail = tail.next

# list2: 2 → 3 → 4 → 5 → 6
head2 = ListNode(2)
tail = head2
for i in range(3, 7):
    tail.next = ListNode(i)
    tail = tail.next

merged_list = obj.mergeTwoLists_Itr(head1, head2)
while merged_list:
    print(merged_list.val, end=' → ' if merged_list.next else '')
    merged_list = merged_list.next