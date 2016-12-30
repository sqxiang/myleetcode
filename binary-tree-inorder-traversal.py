# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#morris solution
#重要的是找到当前节点的前驱，将它前驱的右节点链接到当前节点，这样就保证了往下迭代节点时还能回到当前节点
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result,cur = [],root
        while(cur):
            if cur.left == None:
                result.append(cur.val)
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
                if node.right == None:
                    node.right = cur
                    cur = cur.left
                if node.right == cur:
                    node.right = None
                    result.append(cur.val)
                    cur = cur.right
        return result
			        
