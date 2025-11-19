from typing import Optional
class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def reverse_ll_between_LtoR(self, left:int, right:int, head:Optional[LinkedList])->Optional[LinkedList]:
        dummy = LinkedList(0, head)
        len = right-left+1

        leftPrev, curr = dummy, head
        for i in range(left-1):
            leftPrev =curr
            curr = curr.next
        
        #Now curr="left" and leftPrev="node before theleft"
        # 2.reverse the list from left to right
        prev = None
        for i in range(len):
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt

        #3.update the pointers
        leftPrev.next.next = curr # curr is node after the right
        leftPrev.next = prev  # prev is right
        return dummy.next


# Create linked list: 1 → 2 → 3 → 4 → 5
head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)
head.next.next.next.next.next = None

def print_list(head):
    while head:
        print(head.val, end=' → ' if head.next else '')
        head = head.next

print("Original Linked List:")
print_list(head)

obj = solution()
obj.reverse_ll_between_LtoR(2, 4, head)

print("\n ====================== \n")
print("Reversed between 2 and 4 nodes in a Linked List:")
print_list(head)