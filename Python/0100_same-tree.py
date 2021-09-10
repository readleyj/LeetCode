class Solution:
    def traverse(self, node1, node2):
        if not node1 and not node2:
            return True
        elif (node1 and not node2) or (not node1 and node2):
            return False

        if node1.val != node2.val:
            return False

        return self.traverse(node1.left, node2.left) and self.traverse(node1.right, node2.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.traverse(p, q)
