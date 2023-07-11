# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class 
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque()
        queue.append(root)
        depth = 0

        while queue:
            size = len(queue)
            depth += 1

            for _ in range(size):
                node = queue.popleft()

                if not node.left and not node.right:
                    return depth

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return 0  # In case the tree is empty

root = [3,9,20,null,null,15,7]
r = [TreeNode(i) for i in root]
print()

def minDepth(root):
    if not root:
        return 0

    left = self.minDepth(root.left)
    right = self.minDepth(root.right)

    if root.left and root.right:
        return min(left, right) + 1

    return max(left, right) + 1