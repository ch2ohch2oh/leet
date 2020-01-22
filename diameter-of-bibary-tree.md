# 534 Diameter of binary tree

## Recursion

Intuitive with little memory usage but slow (~5%). 
A more concise version can be found 
[here](https://leetcode.com/problems/diameter-of-binary-tree/discuss/486155/Simple-Python-recursive-solution).

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.largest_diameter(root)
    
    def largest_diameter(self, root):
        if root == None:
            return 0
        left_diameter = self.largest_diameter(root.left)
        right_diameter = self.largest_diameter(root.right)
        root_diameter = self.longest_path(root.left) + self.longest_path(root.right) + 2
        return max(root_diameter, max(left_diameter, right_diameter))
    
    def longest_path(self, root):
        if root == None:
            return -1
        if hasattr(root, 'longest'):
            return root.longest    
        self.longest = max(self.longest_path(root.left), self.longest_path(root.right)) + 1
        # print(f'longest path from {root.val} is {self.longest}')
        return self.longest
```

## Keywords
Tree
