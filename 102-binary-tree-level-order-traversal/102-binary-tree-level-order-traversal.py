# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:  
        if not root:
            return []
        curr = deque([root])
        output = []
        while curr:
            temp = []
            for i in range(len(curr)):
                popped = curr.popleft()
                temp.append(popped.val)
                if popped.left:
                    curr.append(popped.left)
                if popped.right:
                    curr.append(popped.right)
            output.append(temp)
        return(output)
        