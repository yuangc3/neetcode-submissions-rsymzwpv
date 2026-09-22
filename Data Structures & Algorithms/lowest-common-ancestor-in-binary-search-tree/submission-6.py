# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = {root:None}
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node.right:
                queue.append(node.right)
                parents[node.right] = node
                
            
            if node.left:
                queue.append(node.left)
                parents[node.left] = node
                
        
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parents[p]
        
        while q not in ancestor:
            q = parents[q]
        
        return q 

