class Solution:
    def is_leaf(self, node):
        return not node.left and not node.right

    def traverse(self, node, leaf_sums, cur_level=1):
        if not node:
            return None

        if len(leaf_sums) < cur_level:
            leaf_sums.append(0)

        if self.is_leaf(node):
            leaf_sums[cur_level - 1] += node.val

        self.traverse(node.left, leaf_sums, cur_level + 1)
        self.traverse(node.right, leaf_sums, cur_level + 1)

    def deepestLeavesSum(self, root: TreeNode) -> int:
        leaf_sums = []

        self.traverse(root, leaf_sums)

        return leaf_sums[-1]
