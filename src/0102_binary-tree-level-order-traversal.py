class Solution:
    def traverse(self, node, levels, cur_level=1):
        if not node:
            return None
        if cur_level > len(levels):
            levels.append([])

        levels[cur_level - 1].append(node.val)
        self.traverse(node.left, levels, cur_level + 1)
        self.traverse(node.right, levels, cur_level + 1)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []

        self.traverse(root, levels)

        return levels
