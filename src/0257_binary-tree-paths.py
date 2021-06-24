class Solution:
    def traverse(self, node, cur_path, paths):
        if not node:
            return None

        cur_path.append(node.val)

        if not node.left and not node.right:
            paths.append(cur_path[:])
            return None

        self.traverse(node.left, cur_path[:], paths)
        self.traverse(node.right, cur_path[:], paths)

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        paths = []
        self.traverse(root, [], paths)

        return ['->'.join([str(val) for val in path]) for path in paths]
