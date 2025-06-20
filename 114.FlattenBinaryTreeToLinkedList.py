# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                previous = root.left
                while previous.right:
                    previous = previous.right
                previous.right = root.right
                root.right = root.left 
                root.left = None
            root = root.right

            

        

