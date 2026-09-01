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
            node1 = queuep.popleft()
            node2 = queueq.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:         
                return False

            queuep.append(node1.left)
            queueq.append(node2.left)
            queuep.append(node1.right)
            queueq.append(node2.right)
        return not queuep and not queueq


        