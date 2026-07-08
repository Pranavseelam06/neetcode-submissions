# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# I was thinking since we have 1 - 2 - 3 rht that means its 321
# so we can just add the 3 to the 6 and get 9 and since that is less than
# 10 we do nothing and then we go next and add 502 since elss than 10 
# continue but lets say we had 9 an 4 we just take the % 10 and add that 
# if we have a one next we carry over if not we just add the one and return

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carryover = 0
        head = None
        cur = None
        head1 = l1
        head2 = l2
        while head1 is not None or head2 is not None:
            sum = 0
            if carryover == 1:
                sum = sum + 1
            if head1 is not None:
                sum = sum + head1.val
                head1 = head1.next
            if head2 is not None:
                sum = sum + head2.val
                head2 = head2.next
            if sum >= 10:
                carryover = 1
                if sum == 10:
                    sum = 0
                sum = sum % 10
                node = ListNode(sum)
                if head is None:
                    head = node
                    cur = node
                else:
                    cur.next = node
                    cur = cur.next
            else:
                carryover = 0
                node = ListNode(sum)
                if head is None:
                    head = node
                    cur = node
                else:
                    cur.next = node
                    cur = cur.next
        if carryover == 1:
            node = ListNode(1)
            cur.next = node
            cur = cur.next
        return head 