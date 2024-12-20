class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# usado para por em ordem 
def inorder(root):
    if root is not None:
        
        inorder(root.left)

       
        print(str(root.key) + "->", end=' ')

        
        inorder(root.right)


# def para inserção de numeros na arvore
def insert(node, key):

    
    if node is None:
        return Node(key)

  
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# usada para obter o menor valor armazenado
def minValueNode(node):
    current = node

    
    while(current.left is not None):
        current = current.left

    return current


# def usada para deletar numeros da arvore
def deleteNode(root, key):


    if root is None:
        return root

  
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
      
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

       
        temp = minValueNode(root.right)

        root.key = temp.key

        
        root.right = deleteNode(root.right, temp.key)

    return root


#import time foi usado para calcular a diferença de tempo do inicio do codigo até a sua conclusão
import time

from numbers import random_numbers
# 1 bilhão de numeros gerados para ingerir apenas 1 milhão 

start_time = time.time()


tree = None
#for para inserir numeros um por um
for i in random_numbers:
    tree = insert(tree, i)

 #for para deletar numeros um por um   
for i in random_numbers:
    tree = deleteNode(tree, i)
    
    
endtime = time.time()
print("--- %s seconds ---" % (endtime - start_time))
print("Finalizado")