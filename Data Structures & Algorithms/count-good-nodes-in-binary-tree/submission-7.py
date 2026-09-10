# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, total):
           
            if not node:
                return 0

            res = 1 if node.val >= total else 0
            total = max(total, node.val)

            res += dfs(node.left, total)
            res += dfs(node.right, total)
            return res
        return dfs(root, root.val)

      