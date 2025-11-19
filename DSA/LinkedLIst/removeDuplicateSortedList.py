class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def removeDuplicates(self, head:LinkedList)->LinkedList:
        curr = head
        #TC:O(n) and SC:O(1)
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    

obj = solution()
def print_list(head):
    while head:
        print(head.val, end=' → ' if head.next else '')
        head = head.next

# Create linked list: 1 → 1 → 2 → 3 → 3
head = LinkedList(1)
head.next = LinkedList(1)   
head.next.next = LinkedList(2)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(3)
head.next.next.next.next.next = None
print("Original Linked List:")
print_list(head)
# Remove duplicates
updated_head = obj.removeDuplicates(head)
print("\nLinked List after removing duplicates:")
print_list(updated_head)

