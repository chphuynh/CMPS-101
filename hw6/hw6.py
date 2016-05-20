#!/usr/bin/env python3


#creates Node with variables set to null
class Node:
        def __init__(self):
                #left child
                self.left = None
                #right childe
                self.right = None
                #key and value of node
                self.key = None
                self.value = None
                #Boolean variable to check if node is a left child
                self.isLeft = None

class BSTree:

        #initializes empty tree
        def __init__(self):
                self.root = None

        def insert(self, key, value):
                #if root is null, create a node and set root equal
                if self.root is None:
                        tmp = Node()
                        tmp.key = key
                        tmp.value = value
                        self.root = tmp
                        return
                #recursively call insert_recur on the root otherwise
                return self.insert_recur(self.root, key, value)

        def insert_recur(self, curr, key, value):
                if curr is None:
                        return
                if(key < curr.key):
                        if curr.left is None:
                                #if key is less than the current node and the current node does not have a left child
                                #then create a new node and set the current nodes left child to the new node
                                tmp = Node()
                                tmp.key = key
                                tmp.value = value
                                tmp.isLeft = True
                                curr.left = tmp
                                return
                        else:
                                #otherwise move left on the tree and check again
                                return self.insert_recur(curr.left, key, value)
                elif(key > curr.key):
                        if curr.right is None:
                                #if key is greater than the current node and the current node does not have a right child
                                #then create a new node and set the current nodes right child to the new node
                                tmp = Node()
                                tmp.key = key
                                tmp.value = value
                                tmp.isLeft = False
                                curr.right = tmp
                                return
                        else:
                                #otherwise move right on the tree and check again
                                return self.insert_recur(curr.right, key, value)
                else:
                        #if the key is the same as the current node key then add the value to the old value
                        curr.value = curr.value + value
                        return

        def find(self, key):
                #if tree is empty return nothing
                if self.root is None:
                        return
                #returns pointer to found key
                res = self.find_recur(self.root, key)
                return res

        def find_recur(self, curr, key):
                #if key not found return nothing
                if curr is None:
                        return None
                #check left child if the key is less than current node
                if(key < curr.key):
                        return self.find_recur(curr.left, key)
                #check right child if key is greater than current node
                elif(key > curr.key):
                        return self.find_recur(curr.right, key)
                return curr

        def delete(self, key):
                #if root is empty do nothing
                if self.root is None:
                        return
                return self.delete_recur(None, self.root, key)

        def delete_recur(self, parent, curr, key):
                #if key not found do nothing
                if curr is None:
                        return
                #if key is less than current key check left child
                if(key < curr.key):
                        return self.delete_recur(curr, curr.left, key)
                #if key is greater than current key check right child
                elif(key > curr.key):
                        return self.delete_recur(curr, curr.right, key)
                #if key is same as current key do following
                else:
                        #if current node has no children
                        if(curr.left is None) and (curr.right is None):
                                if(parent is None):
                                        #if delete root, set root to null
                                        self.root = None
                                        return
                                else:
                                        if(curr.isLeft):
                                                #if node is left child, set parents left child to null
                                                parent.left = None
                                                return
                                        else:
                                                #if node is right child, set parents right child to null
                                                parent.right = None
                                                return
                        #if node has a right child but no left child
                        elif(curr.left is None) and (curr.right is not None):
                                if(parent is None):
                                        #if deleting root, set root equal to its right child
                                        self.root = self.root.right
                                        return
                                else:
                                        if(curr.isLeft):
                                                #if node is left child, set parents left child to node's right child
                                                parent.left = curr.right
                                                return
                                        else:
                                                #if node is right child, set parents right child to node's right child
                                                parent.right = curr.right
                                                return
                        #if node has a left child but no right child
                        elif(curr.left is not None) and (curr.right is None):
                                if(parent is None):
                                        #if deleting root, set root equal to its left child
                                        self.root = self.root.left
                                        return
                                else:
                                        if(curr.isLeft):
                                                #if node is left child, set parents left child to node's left child
                                                parent.left = curr.left
                                                return
                                        else:
                                                #if node is right child, set parents right child to node's right child
                                                parent.right = curr.left
                                                return
                        #if node has a left and right child
                        else:
                                #find successor
                                successor = self.successor(key)
                                #swap current node with is successor
                                temp = Node()
                                temp.key = successor.key
                                temp.value = successor.value
                                successor.key = curr.key
                                successor.value = curr.value
                                curr.key = temp.key
                                curr.value = temp.value
                                #run delete on the same key
                                return self.delete_recur(curr, curr.right, key)
                                

        def successor(self, key):
                #finds node with key in the tree
                #if the right child of the node is not null 
                if(self.find(key).right is not None):
                        #find the minimum value in the right tree
                        return self.findMin(self.find(key).right)
                #if the right child of node is null
                else:
                    curr = self.root
                    #starting from the top of the tree, traverse down keeping track of each traversal to left child
                    while(curr.key != key):
                        #if key is less than the current node, set the successor equal to the current node and traverse left 
                        if(key < curr.key):
                            successor = curr
                            curr = curr.left
                        #if key is greater than the current node, traverse right
                        elif(key > curr.key):
                            curr = curr.right
                    return successor

        def findMin(self, root):
                #returns the leftmost node in the tree
                if(root.left is None):
                        return root
                return self.findMin(root.left)

        def inOrderTraversal(self):
                return self.inOrder(self.root)

        def inOrder(self, root):
                if(root is None):
                        return
                #recursively run on left child
                self.inOrder(root.left)
                #prints both key and value
                print(str(root.key) + " " + str(root.value))
                #recursively run on right child
                self.inOrder(root.right)

                
        
