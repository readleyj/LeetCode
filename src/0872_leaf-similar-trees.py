class Solution:
    def is_leaf(self, node):
        return not node.left and not node.right

    def traverse(self, node, leaves):
        if not node:
            return None

        if self.is_leaf(node):
            leaves.append(node.val)

        self.traverse(node.left, leaves)
        self.traverse(node.right, leaves)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1, leaves2 = [], []

        self.traverse(root1, leaves1)
        self.traverse(root2, leaves2)

        return leaves1 == leaves2
