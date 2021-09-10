class Solution:
    sum = 0

    def traverse(self, node):
        if not node:
            return None

        if node.val % 2 == 0:
            if node.left:
                left, right = node.left.left, node.left.right
                self.sum += (left.val if left else 0) + \
                    (right.val if right else 0)
            if node.right:
                left, right = node.right.left, node.right.right
                self.sum += (left.val if left else 0) + \
                    (right.val if right else 0)

        self.traverse(node.left)
        self.traverse(node.right)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.traverse(root)

        return self.sum
