class Solution:
    def is_leaf(self, node):
        if not node:
            return False

        return not node.left and not node.right

    def traverse(self, node, cur_path, paths):
        if not node:
            return None

        cur_path.append(str(node.val))

        if self.is_leaf(node):
            paths.append(cur_path[:])

        self.traverse(node.left, cur_path[:], paths)
        self.traverse(node.right, cur_path[:], paths)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = []

        self.traverse(root, [], paths)

        return sum(int(''.join(path), 2) for path in paths)
