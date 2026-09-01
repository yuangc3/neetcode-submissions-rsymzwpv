# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return 0 
        parent = {root:None}
        queue = deque([root])
        while p not in parent or q not in parent:
            temp = queue.popleft()
            if temp.left:
                parent[temp.left] = temp
                queue.append(temp.left)
            if temp.right:
                parent[temp.right] = temp
                queue.append(temp.right)
            
        ancestor = set()
        while p:
            ancestor.add(p)
            p = parent[p]

        while q not in ancestor:
            q = parent[q]
        
        return q

            
