# >>>Victor Andres Barilin<<<
from function import *

# I instantiate a tree
tree = Binary_tree()

# run the app
while True:
    print('-------MENU-------')
    print('>Select one option<')
    print('1- Add')
    print('2- Dell')
    print('3- Find name')
    print('4- View ansestors')
    print('5- View descendant')
    print('6- View with three methods')
    print('------------------')
    op = input('>>> ')

    if op == '1':
        print('------------------')
        run = ''
        while run != 'exit':
            data = input('\nInsert name to load:\n>>> ')
            print('\n')
            tree.add(Node(data))
            run = input('\nPut "exit" for finish start for continue:\n>>> ')
                

    elif op == '2':
        print('------------------')
        data = input('Insert name to delete:\n>>> ')
        tree.dell(data)
    elif op == '3':
        print('------------------')
        data = input('Insert name to search:\n>>> ')
        find = tree.find_data(tree.get_root(), data)
        if find:
            print('\nThe name %s is registered\n'%data)
        else:
            print('\nThe name %s is not registered\n'%data)   
    elif op == '4':
        print('------------------')
        data = input('Insert name to search:\n>>> ')
        tree.see_ansestors(data)
    elif op == '5':
        print('------------------')
        data = input('Insert name to search:\n>>> ')
        tree.see_descendant(data)
    elif op == '6':
        print('\n------------------')
        print('--PREORDER')
        tree.preorder(tree.get_root())
        print('------------------\n')
        print('------------------')
        print('--INORDER')
        tree.inorder(tree.get_root())
        print('------------------\n')
        print('------------------')
        print('--POSTORDER')
        tree.postorder(tree.get_root())
        print('------------------\n')
    else:
        print('------------------')
        print('ERROR: Option not valid')
        print('------------------\n')
        

    