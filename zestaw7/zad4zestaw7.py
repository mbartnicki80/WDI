class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        c_node = self
        if c_node.val == None:
            c_node.val = v
            return
        while (c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def __str__(self):
        c_node = self
        res = ""
        while c_node!=None:
            res += str(c_node.val)+" "
            c_node = c_node.next
        return res
    
def reverse(lista, lista1 = Node()):
    if lista.next == None:
        lista1.append(lista.val)
        return lista1
    reverse(lista.next, lista1)
    lista1.append(lista.val)
    return lista1

if __name__=="__main__":

    lista = Node()
    lista.append(5); lista.append(6); lista.append(7); lista.append(2)
    print(lista)
    print(reverse(lista))