class Solution:
    def deleteNode(self, node):
        runner = node

        while runner.next:
            runner.val = runner.next.val

            if not runner.next.next:
                runner.next = None
                break

            runner = runner.next
