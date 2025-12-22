class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class solution:
    def deleteNthNodefromLast(self, head, n)-> 'Node':
        len = 0
        current = head
        while current:
            len += 1
            current = current.next
        if n > len:
            return -1
        if n == len:
            return head.next
        
        current = head
        for i in range(len - n - 1):
            current = current.next
        
        current.next = current.next.next
        return head

obj = solution()   

def print_list(head):
    while head:
        print(head.val, end=' → ' if head.next else '')
        head = head.next

# Create linked list: 1 → 2 → 3 → 4 → 5
head = LinkedList(1)
head.next = LinkedList(2)
head.next.next = LinkedList(3)
head.next.next.next = LinkedList(4)
head.next.next.next.next = LinkedList(5)
head.next.next.next.next.next = None

print("Original Linked List:")
print_list(head)

# Reverse it
upadted_ll = obj.deleteNthNodefromLast(head, n=2)
#reversed_head1 = obj.deleteNthNodefromLast(head)
print("=====")
print("Reversed Linked List:")
print_list(upadted_ll)
#print_list(upadted_ll)
