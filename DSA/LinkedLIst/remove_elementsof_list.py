
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class solution:
    def removeElements(self, head:ListNode, val:int)->ListNode:
        dummy = ListNode(next=head) #inserted just before the head
        prev, curr = dummy, head

        while curr:
            temp = curr.next
            if curr.val == val:
                prev.next = temp
            else:
                prev = curr
            
            curr = temp
        return dummy.next
    
#obj= solution()

def print_list(head):
    while head:
        print(head.val, end=' → ' if head.next else '')
        head = head.next
    print()

# Create linked list: 1 → 2 → 3 → 4 → 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(2)

print("Original List:")
print_list(head)

# Remove all nodes with value 2
obj= solution()
head = obj.removeElements(head, 2)

print("After Removing 2:")
print_list(head)
""" Original List:
1 → 2 → 3 → 4 → 2
After Removing 2:
1 → 3 → 4 """