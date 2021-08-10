from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> TreeNode:
        # 2i+1 is left, 2i+2 is right. floor(i/2) is parent

        def recursive(i):
            if i > len(inorder):
                return None

            node = TreeNode(inorder[i])

            node.left = recursive(2* i + 1)
            node.right = recursive(2* i + 2)

            return node

        return recursive(0)
