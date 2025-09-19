#4->2->1->3
#1 2 3 4 
#using merge sort
#4->2->null , 1->3->null
#4, 2         1, 3 ----->till here TC:log(n)
#merge them
#2->4->null   1->3->null
#Till final list takes TC : o(n)
#total TC:o(n*logn)

class ListNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class solution:
    def merge_sort_ll(self, head : ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        #split ll into two lists
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        self.merge_sort_ll(left)
        self.merge_sort_ll(right)
        self.merge(left, right)

    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, list1, list2):
        tail= dummy = ListNode()
        while list1 and list2 :
            if list1.val < list2.val :
                tail.next = list1.val
                list1 = list1.next
            else:
                tail.next = list2.val
                list2 = list2.val
            tail = tail.next
        if list1 :
            tail.next = list1
        if list2 :
            tail.next = list2
        return dummy.next


obj = solution()
print(obj.merge_sort_ll[4,2,1,3])

