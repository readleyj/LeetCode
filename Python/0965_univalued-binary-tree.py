class Solution:
    def traverse(self, node, prev_value):
        if not node:
            return True

        if node.val != prev_value:
            return False

        return self.traverse(node.left, node.val) and self.traverse(node.right, node.val)

    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.traverse(root, root.val)
