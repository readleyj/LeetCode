class Solution:
    def is_leaf(self, node):
        return not node.left and not node.right

    def traverse(self, node, target_sum, cur_sum, cur_path, paths):
        if not node:
            return False

        cur_path.append(node.val)
        new_sum = cur_sum + node.val

        if self.is_leaf(node) and new_sum == target_sum:
            paths.append(cur_path[:])
            return None

        self.traverse(node.left, target_sum, new_sum, cur_path[:], paths)
        self.traverse(node.right, target_sum, new_sum, cur_path[:], paths)

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths = []
        self.traverse(root, targetSum, 0, [], paths)
        return paths
