# >>>Victor Andres Barilin<<<

# Creator of node
class Node():
    def __init__(self, data, dad = None, right_son = None, left_son = None):
        self.data = data
        self.dad = dad
        self.right_son = right_son
        self.left_son = left_son

# creator of tree
class Binary_tree():
    def __init__(self):
        self.root = None
        
    def add(self, element):     #add node to tree
        if self.root == None:
            self.root = element
            print('Successful upload!!!')
        else:
            index = self.root
            end = 0
            while end == 0:
                if element.data > index.data:
                    if index.right_son == None:
                        index.right_son = element
                        element.dad = index
                        print('Successful upload!!!')
                        end = 1
                    else:
                        index = index.right_son                
                
                elif element.data < index.data:
                    if index.left_son == None:
                        index.left_son = element
                        element.dad = index
                        print('Successful upload!!!')
                        end = 1
                    else:
                        index = index.left_son

    def dell(self, data):       #dell node to tree
        node = self.find_data(self.root, data)  #I look for the node to delete
        if node:
            if node.left_son == None and node.right_son == None:    #If the node has no children
                node_dad = node.dad
                if node_dad == None:   #I check if the node to delete is the root
                    self.root = None
                    del(node)
                else:
                    if node_dad.right_son == node:  #I check which side of the parent is the node to delete. then I update the links
                        node_dad.right_son = None
                    else:
                        node_dad.left_son = None
                    del(node)

            elif (node.left_son == None and node.right_son != None) or (node.left_son != None and node.right_son == None):  #If the node has a children
                if node.right_son:
                    node_son = node.right_son
                else:
                    node_son = node.left_son
                node_dad = node.dad

                if node_dad == None:    #I check if the node to delete is the root
                    self.root = node_son
                    del(node)
                else:
                    if node_dad.right_son == node:  #I check which side of the parent is the node to delete. then I update the links
                        del(node)
                        node_dad.right_son == node_son
                        node_son.dad = node_dad
                    else:
                        del(node)
                        node_dad.left_son == node_son
                        node_son.dad = node_dad

            elif node.left_son != None and node.right_son != None:    #if the node has two children
                branch = node.right_son     #I select the branch on the right to find the node most to the left
                node_dad = node.dad
                replacement = 0

                while replacement == 0:     #I walk through the branch looking for the node on the left
                    if branch.left_son:
                        branch = branch.left_son
                    else:
                        replacement = 1

                if node_dad == None:        #I check if the element to delete has a parent
                    branch.dad = None                        
                else:
                    if node_dad.right_son == node:  #If it has a parent, I control which side is the node to delete
                        node_dad.right_son = branch
                        branch.dad = node_dad
                    else:
                        node_dad.left_son = branch
                        branch.dad = node_dad
                
                if node.right_son == branch:    #I control that the node to be replaced has its replacement as a child
                    branch.right_son = None
                    branch.left_son = node.left_son
                    node.left_son.dad = branch

                elif node.left_son == branch:   #I control that the node to be replaced has its replacement as a child
                    branch.left_son = None
                    branch.right_son = node.right_son
                    node.right_son.dad = branch
                else:
                    branch.right_son = node.right_son
                    branch.left_son = node.left_son
                if node == self.root:
                    self.root = branch
                del(node)
            print('\nThe name %s was deleted\n'%data)
            
        else:
            print('The data %s was not found'%data)
    #show the data sorted in preorder
    def preorder(self, index):
        if index:
            print(index.data)
            self.preorder(index.left_son) 
            self.preorder(index.right_son)  
    #show the data sorted in inorder
    def inorder(self, index):
        if index:
            self.inorder(index.left_son) 
            print(index.data)
            self.inorder(index.right_son) 
    #show the data sorted in postorder
    def postorder(self, index):
        if index:
            self.postorder(index.left_son) 
            self.postorder(index.right_son) 
            print(index.data)
    
    def find_data(self, root, data):
        if root == None:    #if it does not exist it returns false
            return False
        elif root.data == data:    #when it finds it returns the node
            return root
        elif data < root.data:      #Recursively searches towards the side on which the data is, comparing its value with that of its ansestros
            return self.find_data(root.left_son, data)
        elif data > root.data:
            return self.find_data(root.right_son, data)
    
    def see_descendant(self, data):
        node = self.find_data(self.root, data)  #use the search function to identify the node
        if node:    #check if node exists
            print("%s's desdendant are:"%data)
            self.preorder(node)     #print the offspring in preorder
        else:
            print('The data %s was not found'%data)

    def see_ansestors(self, data):
        node = self.find_data(self.root, data)  #use the search function to identify the node
        if node:    #check if node exists
            print("%s's ansestros are:"%data)
            while node:     #runs through printing parent nodes until there are no more
                print(node.data)
                node = node.dad
        else:
            print('The data %s was not found'%data)
                
    def get_root(self):     #return the nodee root of tree
        return self.root