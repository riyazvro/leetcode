# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        cur=head
        count=0
        while cur and count<k:
            cur=cur.next
            count+=1
        if count<k:
            return head
        prev=None
        cur=head
        for _ in range(k):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        head.next=self.reverseKGroup(cur,k)
        return prev
        