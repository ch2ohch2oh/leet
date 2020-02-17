# 83 Remove duplicates from sorted list

## Two pointers
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # corner case with zero and one node
        if head == None:
            return None
        elif head.next == None:
            return head
        
        first = head
        second = head.next
        while second != None:
            # print(f'second = {second}')
            if first.val == second.val:
                second = second.next
            else:
                first.next = second
                first = first.next
        first.next = None
        return head
```

## Keywords
Two pointers
