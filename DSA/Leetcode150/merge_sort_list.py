#4->2->1->3
#1 2 3 4 
#using merge sort
#4->2->null , 1->3->null
#4, 2         1, 3 ----->till here TC:log(n)
#merge them
#2->4->null   1->3->null
#Till final list takes TC : o(n)
#total TC:o(n*logn)

from typing import Optional

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


class solution:
    def merge_sort_ll(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # split ll into two lists
        left = head
        mid = self.getMid(head)
        right = mid.next
        mid.next = None

        left_sorted = self.merge_sort_ll(left)
        right_sorted = self.merge_sort_ll(right)
        return self.merge(left_sorted, right_sorted)

    def getMid(self, head: ListNode) -> ListNode:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

def build_linked_list(values) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

obj = solution()
head = build_linked_list([4,2,1,3])
sorted_head = obj.merge_sort_ll(head)
print(linked_list_to_list(sorted_head))

