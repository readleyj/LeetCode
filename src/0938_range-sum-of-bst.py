class Solution:
    range_sum = 0

    def traverse(self, node, low, high):
        if not node:
            return None

        self.range_sum += node.val * (low <= node.val <= high)

        self.traverse(node.left, low, high)
        self.traverse(node.right, low, high)

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.traverse(root, low, high)
        return self.range_sum
