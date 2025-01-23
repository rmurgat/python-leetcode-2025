from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeBundle01:
    
    def insertBST(self, root: TreeNode, val: int):
        if root is None:
            root = TreeNode(val)
            return
        
        if val < root.val:
            if root.left:
                self.insertBST(root.left, val)
            else:
                root.left = TreeNode(val)
        else:
            if root.right:
                self.insertBST(root.right, val)
            else:
                root.right = TreeNode(val)

    def insertInOrder(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        it = iter(nums)
        root = TreeNode(next(it))
        q = [root]
        for node in q:
            val = next(it, None)
            if val is not None:
                node.left = TreeNode(val)
                q.append(node.left)
            val = next(it, None)
            if val is not None:
                node.right = TreeNode(val)
                q.append(node.right)
        return root

    def prettyTree(self, root: TreeNode, last=True, header='', side=''):
       elbow = "└──"
       pipe = "│  "
       tee = "├──"
       blank = "   "
       if root is None: return
       print(header + (elbow if last else tee) + str(root.val)+("" if side=='' else "-"+side))
       if root.left: self.prettyTree(root=root.left, last=False if root.right else True, header=header + (blank if last else pipe),side="l" )
       if root.right: self.prettyTree(root=root.right, last=True, header=header + (blank if last else pipe), side="r")    

    def printPrettyTreeRight(self, root: TreeNode, last=True, header='', side=''):
       elbow = "└──"
       pipe = "│  "
       tee = "├──"
       blank = "   "
       if root is None: return
       print(header + (elbow if last else tee) + str(root.val)+("" if side=='' else "-"+side))
       if root.right: self.prettyTree(root=root.right, last=True, header=header + (blank if last else pipe), side="r")    


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1) 
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def depth(root) -> int:
            nonlocal ans
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            ans = max(ans, left+right)
            return max(left+1, right+1)
        depth(root)
        return ans

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        def depth(root: Optional[TreeNode]) -> int:
            nonlocal ans
            if not root: return 0
            left = depth(root.left)
            right = depth(root.right)
            b = abs(left - right)
            if ans and b>1: ans = False
            return max(left+1, right+1)
        
        depth(root)
        return ans

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes=[]
        # search subroot 
        def search(root: Optional[TreeNode], val) -> None:
            if root is None: return 
            if root.val == val: nodes.append(root)
            search(root.left, val)
            search(root.right, val)

        # compare treeNodes
        def compare(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if root1 is None or root2 is None:
                if root1!=root2: return False
                return True
            ans = True
            if root1.val != root2.val: ans = False
            if ans and compare(root1.left, root2.left)==False: ans = False
            if ans and compare(root1.right, root2.right)==False: ans = False
            return ans
        search(root, subRoot.val)
        for n in nodes:
            if compare(n, subRoot): return True

        return False