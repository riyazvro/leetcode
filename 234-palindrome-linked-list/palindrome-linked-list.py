# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow,fast=head,head
        # prev=None
        while fast and fast.next:
            # prev=slow
            slow=slow.next
            fast=fast.next.next
        cur=slow
        prev=None
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        left,right=head,prev
        while right:
            if right.val!=left.val:
                return False
            right=right.next
            left=left.next
        return True
        
            
        
        