class Solution:
    def rangeSumBST(self, n: Optional[TreeNode], l: int, h: int) -> int:
        return self.rangeSumBST(n.left,l,h)+n.val*(l<=n.val<=h)+self.rangeSumBST(n.right,l,h) if n else 0