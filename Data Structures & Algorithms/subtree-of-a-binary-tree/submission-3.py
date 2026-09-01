# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same_tree(p, q):
            queue1 = deque([p])
            queue2 = deque([q])

            while queue1 and queue2:
                node1 = queue1.popleft()
                node2 = queue2.popleft()

                if not node1 and not node2:
                    continue

                if not node1 or not node2:
                    return False

                if node1.val != node2.val:
                    return False

                queue1.append(node1.left)
                queue1.append(node1.right)

                queue2.append(node2.left)
                queue2.append(node2.right)

            return not queue1 and not queue2
        if not subRoot:
            return True
        if not root:
            return False
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
               if same_tree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False
        
                            