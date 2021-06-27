class Solution:
    MAX_DEPTH = -1

    def traverse(self, node, cur_depth=1):
        if not node:
            return None

        self.MAX_DEPTH = max(self.MAX_DEPTH, cur_depth)

        self.traverse(node.left, cur_depth + 1)
        self.traverse(node.right, cur_depth + 1)

    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root)

        return self.MAX_DEPTH
