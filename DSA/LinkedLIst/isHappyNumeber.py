# Using slow and fast pointer method
#o(n) and o(1)
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isHappy_num(self, n:int)->bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit = number % 10
                total_sum += digit ** 2
                number //= 10
            return total_sum

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

        return fast == 1

obj = Solution()   
print(obj.isHappy_num(19)) # True
print(obj.isHappy_num(2)) #False

# Create nodes
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

# Link nodes: 1 → 2 → 3 → 4 → 2 (cycle)
a.next = b
b.next = c
c.next = d
d.next = b  # Cycle here
#d.next = None  # No cycle

#print("Cycle detected:", obj.hasCycle(a))  # ➜ True