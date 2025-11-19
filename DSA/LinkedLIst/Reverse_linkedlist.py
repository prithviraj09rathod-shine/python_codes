#reverse linked list

class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class solution:
    def reverse_list(self, head:LinkedList)->LinkedList:
        prev = next = None
        curr = head
        #TC:O(n) and SC:O(1)
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    #Tc:o(n), sc:o(n) beacuse for n nodes there will be n recursive calls
    def reverse_list_recursive(self, head: LinkedList)->LinkedList:
        if not head or head.next:
            return None

        #newHead = head
        
        newHead = self.reverse_list(head.next)
        
        head.next.next = head
        head.next = None
        return newHead

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
reversed_head = obj.reverse_list(head)
#reversed_head1 = obj.reverse_list_recursive(head)
print("=====")
print("Reversed Linked List:")
print_list(reversed_head)
#print_list(reversed_head1)

