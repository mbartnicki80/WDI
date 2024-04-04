class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        c_node = self
        while c_node.next!=None:
            c_node = c_node.next
        c_node.next = Node(v)

    def pop_val(self, v):
        c_node = self
        while(c_node.next!=None and c_node.next.val!=v):
            c_node = c_node.next
        if c_node.next.val==v:
            c_node.next = c_node.next.next 
    
    def __str__(self):
        c_node = self
        res = ""
        while(c_node!=None):
            if c_node.val!=None:
                res += str(c_node.val)+" "
            c_node = c_node.next
        return res

def funk(lista, v):

    while(lista.next!=None and lista.next.val!=v):
        lista = lista.next
    if lista.next!=None:
        lista.pop_val(v)
    else:
        lista.append(v)
    return lista

if __name__=="__main__":
    lista = Node()
    lista.append(5); lista.append(3); lista.append(6)
    print(lista)
    funk(lista, 7)
    print(lista)
    funk(lista, 3)
    print(lista)