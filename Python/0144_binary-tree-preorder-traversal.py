class Solution:
    def traverse(self, node, traversal):
        if not node:
            return None

        traversal.append(node.val)
        self.traverse(node.left, traversal)
        self.traverse(node.right, traversal)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []

        self.traverse(root, traversal)
        return traversal
