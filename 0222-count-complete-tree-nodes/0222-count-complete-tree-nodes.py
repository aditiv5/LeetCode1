# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0 # Used to maintain the count of the nodes

    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.count_nodes(root) # Used to call the recuresive function initially
        return self.count

    def count_nodes(self,root):
        if root:
            self.count+=1
            if root.left:
                self.count_nodes(root.left)
            if root.right:
                self.count_nodes(root.right)
        return 