class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        c_node = self
        while (c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def __str__(self):
        c_node = self
        res = ""
        while(c_node.next!=None):
            res += str(c_node.next.val)+" "
            c_node = c_node.next
        return res
    
    def insert(self, v):
        c_node = self
        while (c_node.next!=None):
            if c_node.next.val==v:
                return
            if c_node.next.val>v:
                c_node.next, c_node.next.next = Node(v), c_node.next
                return
            c_node = c_node.next
        c_node.next, c_node.next.next = Node(v), c_node.next
    
    def search(self, v):
        c_node = self
        while (c_node.next!=None):
            if c_node.next.val>v:
                return False
            if c_node.next.val==v:
                return True
            c_node = c_node.next
        return False

#lista 2 nieuporzadkowana
def funk(lista1, lista2):
    
    nowa = Node()
    wskaznik = nowa
    nowa.next = lista1.next
    lista2 = lista2.next

    while (lista2!=None):
        val = lista2.val
        nowa.insert(val)
        lista2 = lista2.next
    return wskaznik

if __name__=="__main__":
    lista1 = Node()
    lista2 = Node()
    lista1.append(2); lista1.append(3); lista1.append(5); lista1.append(7); lista1.append(11)
    lista2.append(8); lista2.append(2); lista2.append(7); lista2.append(4); lista2.append(12)
    print(lista1)
    print(lista2)
    print(funk(lista1, lista2))
    