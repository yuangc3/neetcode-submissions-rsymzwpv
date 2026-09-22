# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q1:
            node = q1.popleft()
            node1 = q2.popleft()

            if not node and not node1:
                continue
            if not node or not node1:
                return False
            
            if node.val != node1.val:
                return False

            q1.append(node.left)
            q1.append(node.right)
            q2.append(node1.left)
            q2.append(node1.right)
        return True