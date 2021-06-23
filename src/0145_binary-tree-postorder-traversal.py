class Solution:
    def traverse(self, node, traversal):
        if not node:
            return None

        self.traverse(node.left, traversal)
        self.traverse(node.right, traversal)
        traversal.append(node.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        self.traverse(root, traversal)

        return traversal
