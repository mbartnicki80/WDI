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
    
def funk(lista):
    tab = [Node() for i in range(10)]
    while(lista!=None):
        tab[(lista.val)%10].append(lista.val)
        lista = lista.next
    lista1 = Node()
    for i in range(10):
        if tab[i].val!=None:
            lista1.append(tab[i])
    return lista1
        

if __name__=="__main__":

    lista = Node()
    lista.append(12); lista.append(5); lista.append(51); lista.append(6); lista.append(7); lista.append(2); lista.append(12); lista.append(66)
    print(lista)
    print(funk(lista))