def findTarget(root, k: int) -> bool:
    def preorder_traversal(root):
        if root is None:
            return []

        left = preorder_traversal(root.left)
        val = [root.val]
        right = preorder_traversal(root.right)

        return left + val + right

    A = preorder_traversal(root)
    start = 0
    end = len(A) - 1

    while start < end:
        val = A[start] + A[end]
        if val == k:
            True
        elif val > k:
            end -= 1
        else:
            start += 1
    return False

print
