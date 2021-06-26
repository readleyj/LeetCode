class Solution:
    left_leaf_sum = 0

    def is_leaf(self, node):
        return not node.left and not node.right

    def traverse(self, node, is_left=False):
        if not node:
            return None

        if is_left and self.is_leaf(node):
            self.left_leaf_sum += node.val

        self.traverse(node.left, is_left=True)
        self.traverse(node.right, is_left=False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.traverse(root)

        return self.left_leaf_sum
