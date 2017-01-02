# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = []
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        if root is None:
            return True
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            p,q = stack.pop(),stack.pop()

            if p is None and q is None:
                continue

            if p is None or q is None or p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)

        return True

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSym(root.left,root.right)

    def isSym(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None or p.val != q.val:
            return False

        return self.isSym(p.left,q.right) and self.isSym(p.right,q.left)
