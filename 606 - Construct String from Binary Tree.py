"""
You need to construct a string consists of parenthesis and integers
from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()".
And you need to omit all the empty parenthesis pairs that don't affect the
one-to-one mapping relationship between the string and the original binary
tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one
mapping relationship between the input and the output.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        return t

    # inorder isn't part of the leetcode problem, for testing purposes only
    def inorder(self, node):
        # prints in numerical order
        if node is not None:
            # Checks left and right nodes, if they don't exist they won't be
            # printed
            self.inorder(node.left)
            print(node.val)
            self.inorder(node.right)

    #create isn't part of leetcode problem, for testing purposes only
    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
            while 1:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

solution = Solution()
arr = [7, 2, 3, 6, 9, 10, 11, 15, 19, 21, 100]
for i in arr:
    solution.create(i)
print(solution.tree2str("123"))