# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queuep = deque([p])
        queueq = deque([q])

        while queuep and queueq:
            node = queuep.popleft()
            node1 = queueq.popleft()
            if not node and not node1:
                continue
            if not node or not node1:
                return False
            if node.val != node1.val:
                return False
            queuep.append(node.left)
            queuep.append(node.right)
            queueq.append(node1.left)
            queueq.append(node1.right)
        return True