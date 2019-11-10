# Add two numbers stored in two linked list
# Keyword: linked list
# Caution: For 5 + 5 = 10, the two input linked lists are of length 1 while the resulting linked
#          linked list is of length 2. The overflow/carry bit needs to be handled properly.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        multi = 1
        carry = 0
        # The first node is not used
        head = ListNode(0)
        prev = head
        while l1 and l2:
            s = l1.val + l2.val + carry
            carry = s // 10
            s %= 10
            prev.next = ListNode(s)
            prev = prev.next
            multi *= 10
            l1 = l1.next
            l2 = l2.next
        rest = None
        if l1:
            rest = l1
        if l2:
            rest = l2
        while rest:
            s = rest.val + carry
            carry = s // 10
            s %= 10
            prev.next = ListNode(s)
            prev = prev.next
            multi *= 10
            rest = rest.next
        # Deal with the highest bit
        if carry:
            prev.next = ListNode(carry)
        return head.next
    
