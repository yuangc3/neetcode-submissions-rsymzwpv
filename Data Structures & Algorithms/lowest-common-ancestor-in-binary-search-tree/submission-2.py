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
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q not in ancestors:
            q = parents[q]
        return q 