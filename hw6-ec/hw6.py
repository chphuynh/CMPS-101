# Red-Black Tree implemetation of HW6
# Christopher Huynh chphuynh
# Oliver Rene orene

#NIL Node for Red-Black Tree
class NilNode:
    def __init__(self):
        #NIL Node has a color so we can check Red-Black Tree Properties
        self.color = 'Black'

NIL = NilNode()

class Node:
    #Initializes node with Node(key, value) and other paramenters if inputed
    def __init__(self, key, value, color = 'Red', left = NIL, right = NIL, parent = NIL):
        self.key = key
        self.value = value
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent

class BSTree():

    #Initializes empty tree with NIL Node
    def __init__(self):
        self.root = NIL

    #Performs left rotation of tree
    def left_rotate(self, x):
        assert (x.right != NIL)
        y = x.right
        #x's right subtree is now y's left subtree
        x.right = y.left
        if y.left != NIL:
            y.left.parent = x
        #y's parent is now x's parent
        y.parent = x.parent
        #if we are at root set root to y
        if x.parent == NIL:
            self.root = y
        #if x is left child, set x's parent's left child to y
        elif x == x.parent.left:
            x.parent.left = y
        #if x is right child, set x's parent's right child to y
        else:
            x.parent.right = y
        #set y's left child to x
        y.left = x
        x.parent = y

    #Performs right rotation of tree
    def right_rotate(self, x):
        assert (x.left != NIL)
        y = x.left
        #x's left subtree is now y's right subtree
        x.left = y.right
        if y.right != NIL:
            y.right.parent = x
        #y's parent is now x's parent
        y.parent = x.parent
        #if we are at root set root to y
        if x.parent == NIL:
            self.root = y
        #if x is right child, set x's parent's right child to y
        elif x == x.parent.right:
            x.parent.right = y
        #if x is left child, set x's parent's left child to y
        else:
            x.parent.left = y
        #set y's right child to x
        y.right = x
        x.parent = y

    #inserts key with value into tree
    def insert(self, key, value):
        #creates node to be added
        temp = Node(key, value)
        y = NIL
        x = self.root
        #finds location to insert node
        while x != NIL:
            y = x
            if temp.key < x.key:
                x = x.left
            elif temp.key > x.key:
                x = x.right
            else:
                break
        temp.parent = y
        #if tree is empty, set the root to node
        if y == NIL:
            self.root = temp
            return self.RB_Fix(self.root)
        #if node key is less than location key, insert node to left
        elif temp.key < y.key:
            y.left = temp
            #perform Red-Black Tree Fix
            return self.RB_Fix(y.left)
        #if node key is greater than location key, insert node to right
        elif temp.key > y.key:
            y.right = temp
            #perform Red-Black Tree Fix
            return self.RB_Fix(y.right)
        #if node key is equal to location key, add the value to the current location value
        else:
            y.value = y.value + value

    #Performs a series of rotations to ensure Red-Black Tree Properties are satisfied
    def RB_Fix(self, x):
        x.color = 'Red'
        while x != self.root and x.parent.color == 'Red':
            if x.parent == x.parent.parent.left:
                #If x's parent is a left child, y is x's right uncle
                y = x.parent.parent.right
                if y.color == 'Red':
                    #case 1 of insertion
                    #Change colors
                    x.parent.color = 'Black'
                    y.color = 'Black'
                    x.parent.parent.color = 'Red'
                    #Move x up tree
                    x = x.parent.parent
                else:
                    #y is a black node
                    if x == x.parent.right:
                        #x is right child
                        #case 2 of insertion
                        #move x up and rotate
                        x = x.parent
                        self.left_rotate(x)
                    #case 3 of insertion
                    x.parent.color = 'Black'
                    x.parent.parent.color = 'Red'
                    self.right_rotate(x.parent.parent)
            else:
                #If x's parent is a right child, y is x's left uncle
                y = x.parent.parent.left
                if y.color == 'Red':
                    #case 1 of insertion
                    #Change colors
                    x.parent.color = 'Black'
                    y.color = 'Black'
                    x.parent.parent.color = 'Red'
                    #Move x up tree
                    x = x.parent.parent
                else:
                    #y is a black node
                    if x == x.parent.left:
                        #x is a left child
                        #case 2 of insertion
                        #move x up and rotate
                        x = x.parent
                        self.right_rotate(x)
                    #case 3 of insertion
                    x.parent.color = 'Black'
                    x.parent.parent.color = 'Red'
                    self.left_rotate(x.parent.parent)
        #Ensure root color is black
        self.root.color = 'Black'

    def delete(self, key):
        #finds location of key to delete
        n = self.find(key)
        #if location has no children set y to n
        if n.left == NIL or n.right == NIL:
            y = n
        #else set y to its successor
        else:
            y = self.successor(key)
        #if y has a left child set x equal to left child
        if y.left != NIL:
            x = y.left
        #if y does not have left child, set x equal to right child
        #regardles of if right child is NIL or not
        else:
            x = y.right
        x.parent = y.parent
        #If the key to delete is the root, set root to x
        if y.parent == NIL:
            self.root = x
        else:
            #if y is a left child, set y's parent's left child to x
            if y == y.parent.left:
                y.parent.left = x
            #if y is a right child, set y's parent's right child to x
            else:
                y.parent.right = x
        #set the locations value and key to y
        if y != n:
            n.key = y.key
            n.value = y.value
        #if y is black perform Red Black Tree Fix
        if y.color == 'Black':
            self.RB_Fix_Delete(x)

    def RB_Fix_Delete(self, x):
        while x != self.root and x.color == 'Black':
            if x == x.parent.left:
                #if x is a left child set w to x's parent's right child
                w = x.parent.right
                if w.color == 'Red':
                    #case 1 of deletion
                    #Change colors
                    w.color = 'Black'
                    x.parent.color = 'Red'
                    #perform rotation
                    self.left_rotate(x.parent)
                    #move w up tree
                    w = x.parent.right
                if w.left.color == 'Black' and w.right.color == 'Black':
                    #case 2 of deletion
                    #Change w color
                    w.color = 'Red'
                    #move x up tree
                    x = x.parent
                else:
                    #Either w's left child or w's right child is Red
                    if w.right.color == 'Black':
                        #if w's right child is black
                        #case 3 of deletion
                        #Change colors
                        w.left.color = 'Black'
                        w.color = 'Red'
                        #Perform rotation
                        self.right_rotate(w)
                        #move w up tree
                        w = x.parent.right
                    #Case 4 of deletion
                    #Change colors
                    w.color = x.parent.color
                    x.parent.color = 'Black'
                    w.right.color = 'Black'
                    #Perform rotation
                    self.left_rotate(x.parent)
                    #move x to root of tree
                    x = self.root
            else:
                #if x is a right child set w to x's parent's right child
                w = x.parent.left
                if w.color == 'Red':
                    #case 1 of deletion
                    #change colors
                    w.color = 'Black'
                    x.parent.color = 'Red'
                    #perform rotation
                    self.right_rotate(x.parent)
                    #move w up tree
                    w = x.parent.left
                if w.left.color == 'Black' and w.right.color == 'Black':
                    #case 2 of deletion
                    #change w color
                    w.color = 'Red'
                    #move x up tree
                    x = x.parent
                else:
                    #Either w's left child or w's right child is red
                    if w.left.color == 'Black':
                        #if w's left child is black
                        #case 3 of deletion
                        #change colors
                        w.right.color = 'Black'
                        w.color = 'Red'
                        #perform rotation
                        self.left_rotate(w)
                        #move w up tree
                        w = x.parent.left
                    #Case 4 of deletion
                    #Change colors
                    w.color = x.parent.color
                    x.parent.color = 'Black'
                    w.left.color = 'Black'
                    #perform rotation
                    self.right_rotate(x.parent)
                    #move x to root of tree
                    x = self.root
        #set root of tree to black
        x.color = 'Black'

    #Prints the tree in order
    def inOrderTraversal(self):
        return self.inOrder(self.root)

    def inOrder(self, root):
        if(root == NIL):
            return
        #recursively run on left child
        self.inOrder(root.left)
        #Print key and value
        print(str(root.key) + " " + str(root.value))
        #recursively run on right child
        self.inOrder(root.right)

    def find(self, key):
        y = NIL
        x = self.root
        #Goes through tree and finds position of key
        while x != NIL:
            y = x
            #key less than current position move left
            if key < x.key:
                x = x.left
            #key greater than current position move right
            elif key > x.key:
                x = x.right
            #key equal to current position break
            else:
                break
        #if key found return position
        if key == y.key:
            return y
        #if not found return NIL
        else:
            return NIL

    def successor(self, key):
        #finds location of key
        x = self.find(key)
        #if x has a right child, return the minimum value in x's right subtree
        if x.right != NIL:
            return self.findMin(x.right)
        y = x.parent
        #otherwise traverse up tree until a right turn is made
        while y != NIL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, key):
        #finds location of key
        x = self.find(key)
        #if x has a left child, return maximum value in x's left subtree
        if x.left != NIL:
            return self.findMax(x.left)
        y = x.parent
        #otherwise traverse up tree until a left turn is made
        while y != NIL and x == y.left:
            x = y
            y = y.parent
        return y

    def findMin(self, curr):
        #returns the left most node in tree
        while curr.left != NIL:
            curr = curr.left
        return curr

    def findMax(self, curr):
        #returns right most node in tree
        while curr.right != NIL:
            curr = curr.right
        return curr
