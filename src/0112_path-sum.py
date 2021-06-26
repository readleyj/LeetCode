class Solution:
    def is_leaf(self, node):
        return not node.left and not node.right

    def traverse(self, node, target_sum, cur_sum=0):
        if not node:
            return False

        new_sum = cur_sum + node.val

        if self.is_leaf(node) and new_sum == target_sum:
            return True

        return self.traverse(node.left, target_sum, new_sum) or self.traverse(node.right, target_sum, new_sum)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.traverse(root, targetSum)
