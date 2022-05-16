from collections import *
 
class Node:
    def __init__(self, data):
        self.data = data
        self.right = self.left = None
 
class LevelOrderTraversal:
     
    def __init__(self): 
        self.root = None
 
    def traverse(self, root):
        bfs = []
        if root is None:
            return bfs
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current.data)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            bfs.append(current_level)
        return bfs
     
if __name__ == '__main__':
    tree = LevelOrderTraversal()
    tree.root = Node(4)
    tree.root.left = Node(6)
    tree.root.right = Node(8)
    tree.root.left.left = Node(9)
    tree.root.right.left = Node(5)
    tree.root.right.right = Node(7)
    ans = tree.traverse(tree.root)
    print(ans)
    for level in ans:
        for node in level:
            print(node, end = " ")
        print()

#shortest path to get food
#bfs
#Input: grid = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
# Output: 3
# Explanation: It takes 3 steps to reach the food.
# Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
# Output: -1
# Explanation: It is not possible to reach the food.
# Input: grid = [["X","X","X","X","X","X","X","X"],["X","*","O","X","O","#","O","X"],["X","O","O","X","O","O","X","X"],["X","O","O","O","O","#","O","X"],["X","X","X","X","X","X","X","X"]]
# Output: 6
# Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.

# class Node:
#     def __init__(self,x,y,time):
#         self.x=x
#         self.y=y
#         self.time=time

# class Solution:
#     def orangesRotting(self, grid):
#         rows=len(grid)
#         cols=len(grid[0])
#         queue=deque()
        
#         for i in range (rows):
#             for j in range (cols):
#                 if grid[i][j]=="*":
#                     node=Node(i,j,0)
#                     queue.append(node)
        
#         ans=0
#         while queue:
#             curr_node=queue.popleft()
#             x, y, time= curr_node.x, curr_node.y, curr_node.time
            
#             if x-1>=0 and grid[x-1][y]==None:
#                 grid[x-1][y]=2
#                 node= Node(x-1, y, time+1)
#                 queue.append(node)
#                 ans=time+1
                
#             if x+1< rows and grid[x+1][y]==None:
#                 grid[x+1][y]=2
#                 node= Node(x+1, y, time+1)
#                 queue.append(node)
#                 ans=time+1
                
#             if y-1>=0 and grid[x][y-1]==None:
#                 grid[x][y-1]=2
#                 node= Node(x, y-1, time+1)
#                 queue.append(node)
#                 ans=time+1
                
#             if y+1< cols and grid[x][y+1]==None:
#                 grid[x][y+1]=2
#                 node= Node(x, y+1, time+1)
#                 queue.append(node)
#                 ans=time+1
                
#         for i in range (rows):
#             for j in range (cols):
#                 if grid[i][j]==1:
#                     return -1
        
#         return ans

# grid=[["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
    