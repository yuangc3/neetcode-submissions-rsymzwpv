# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
         
        def dfs(node):
            if not node:
                return True
            
            left = self.get_height(node.left)
            right = self.get_height(node.right)

            if abs(left- right) > 1:
                return False

            return dfs(node.left) and dfs(node.right)
        return dfs(root)
        
    def get_height(self, node):
        if not node:
            return 0 
        
        return 1+max(self.get_height(node.left), self.get_height(node.right))