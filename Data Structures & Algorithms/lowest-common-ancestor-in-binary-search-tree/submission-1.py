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
        while p not in parents or q not in parents:
            node = queue.popleft()

            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)

        ancestor = set()
        while p:
            ancestor.add(p)
            p = parents[p]

        while q not in ancestor:
            q = parents[q]
        
        return q 
