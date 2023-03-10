list = []
menu_in = 0
class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)

    def print_list(node):
        while node is not None:
            print(node, end=" ")
            node = node.next
        print()

while menu_in != 4:
    print('what do you want to do?')
    print('1. add node, 2. delete node, 3. print list, 4. exit')
    menu_in = int(input())
    if menu_in == 1:
        print('what cargo you want to add?')
        add_in = input()
        list.append(Node(add_in))

    if menu_in == 2:
        print('what element in the list do you want to delete?')
        del_in = input()
        list.remove(Node(del_in))
    if menu_in == 3:
        print(list)
    if menu_in == 4:
        break
    else:
        print('wrong input')


#node1 = Node('cargo of node1')
#node2 = Node('cargo of node2')
#node3 = Node('cargo of node3')
#node1.next = node2
#node2.next = node3

#print(node1.cargo,node1.next)
#print(node2.cargo,node2.next)
#print(node3.cargo,node3.next)

#print(node1.print_list())