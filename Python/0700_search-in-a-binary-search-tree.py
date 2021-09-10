class Solution:
    def traverse(self, node, search_val):
        if not node:
            return None

        if node.val == search_val:
            return node

        if search_val > node.val:
            to_search = node.right
        elif search_val < node.val:
            to_search = node.left

        if (search_result := self.traverse(to_search, search_val)):
            return search_result

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.traverse(root, val)
