class Solution:
    def traverse(self, node, traversal):
        if not node:
            return None

        self.traverse(node.left, traversal)
        traversal.append(node.val)
        self.traverse(node.right, traversal)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        self.traverse(root, traversal)

        return traversal
