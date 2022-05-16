''' 
CONSTRUCT BST
FIND MAX ELE
FIND MIN ELE
PREORDER
INORDER
SEARCH
INSERT
DELETE
VALIDATE BST
'''
import math

class TreeNode:
    def __init__(self, data, left, right):
        self.data= data
        self.left=left
        self.right =right

def construct(arr, low, high):
    if (low> high):
        return None

    mid=(low+high)//2
    root_value= arr[mid]
    left_node = construct( arr, low , mid-1)
    right_node = construct( arr, mid+1 , high)
    new_node= TreeNode (root_value, left_node, right_node)
    return new_node

def find_max(root):
    if root is None:
        return -1
    if (root.right is not None):
        return find_max(root.right)
    else:
        return (root.data)

def find_min(root):
    if root is None:
        return -1
    if (root.left is not None):
        return find_min(root.left)
    else:
        return (root.data)

def pre_order(root):
    if (root==None):
        return 
    print (root.data, end=" ")
    pre_order(root.left)
    pre_order(root.right)

def in_order(root):
    if (root==None):
        return
    in_order(root.left)
    print (root.data, end=" ")
    in_order(root.right)

def search(root, val):
    if root is None:
        return None
    if val> root.data:
        return search(root.right, val)
    elif val< root.data:
        return search(root.left, val)
    else:
        return root

def insert( root, val):
    if root is None:
        return TreeNode(val, None, None)
    if val<root.data:
        root.left = insert(root.left, val)
    elif val> root.data:
        root.right = insert (root.right, val)
    else:
        pass
    return root

def delete(root, val):
    if root is None:
        return None
    if val>root.data:
        root.right= delete(root.right, val)
    elif val<root.data:
        root.left= delete(root.left, val)
    else:
        if root.left is not None and root.right is not None:
            left_max= find_max(root.left)
            root.data=left_max
            root.left= delete(root.left, left_max)
            return root
        elif root.left is not None:
            return root.left
        elif root.right is not None:
            return root.right
        else:
            return None
    return root

def checkvalidation(root, min_value, max_value):
    if root is None:
        return True
    if root.data > min_value and root.data<max_value:
        return checkvalidation (root.left, min_value, root.data) and checkvalidation(root.right, root.data, max_value)
    return False

def validate(root):
    return checkvalidation(root, -math.inf, math.inf)
        

if __name__=='__main__':
    arr=[10,30,40,50,60,70,20,80,90]
    root= construct(arr, 0, len(arr)-1)
    pre_order(root)
    print()
    in_order(root)
    print()
    print(find_max(root))
    print(find_min(root))
    print(search(root,60))
    print(insert(root,67))
    in_order(root)
    print()
    print(delete(root,67))
    in_order(root)
    print()
    print (validate(root))