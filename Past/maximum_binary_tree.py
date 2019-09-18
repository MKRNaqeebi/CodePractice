# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def add_left(self, node, array):
        
        max_index = array.index(max(array))
        node.left = TreeNode(array[max_index])
        if array[:max_index]:
            self.add_left(node.left, array[:max_index])
        if array[max_index+1:]:
            self.add_right(node.left, array[max_index+1:])
    def add_right(self, node, array):

        max_index = array.index(max(array))
        node.right = TreeNode(array[max_index])
        if array[:max_index]:
            self.add_left(node.right, array[:max_index])
        if array[max_index+1:]:
            self.add_right(node.right, array[max_index+1:])


    def print_node(self, node):
        print(node.val)
        if node.right:
            self.print_node(node.right)
        if node.left:
            self.print_node(node.left)

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        max_index = nums.index(max(nums))

        node = TreeNode(nums[max_index])
        if nums[:max_index]:
            self.add_left(node, nums[:max_index])
        if nums[max_index+1:]:
            self.add_right(node, nums[max_index+1:])
        self.print_node(node)
        
        return node


solution = Solution()
solution.constructMaximumBinaryTree([1,2,5,6,8,7,3,4])
