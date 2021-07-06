class Solution:
    def traverse(self, node, level_sums, cur_level=1):
        if not node:
            return None

        if cur_level not in level_sums:
            level_sums[cur_level] = 0

        level_sums[cur_level] += node.val

        self.traverse(node.left, level_sums, cur_level + 1)
        self.traverse(node.right, level_sums, cur_level + 1)

    def maxLevelSum(self, root: TreeNode) -> int:
        level_sums = dict()

        self.traverse(root, level_sums)

        return max(level_sums, key=level_sums.get)
