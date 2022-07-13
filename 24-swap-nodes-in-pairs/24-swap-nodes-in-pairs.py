# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        pre,cur,ans=None,head,head.next
        while cur and cur.next:
            adj=cur.next
            if pre:
                pre.next=adj
            cur.next,adj.next=adj.next,cur
            pre,cur=cur,cur.next
        return ans or head