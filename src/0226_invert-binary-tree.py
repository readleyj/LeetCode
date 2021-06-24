class Solution:
    def traverse(self, node):
        if not node:
            return None

        node.left, node.right = node.right, node.left

        self.traverse(node.left)
        self.traverse(node.right)

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.traverse(root)

        return root
