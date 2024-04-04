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
    
    def pop(self, v):
        c_node = self
        while (c_node.next!=None):
            if c_node.next.val==v:
                c_node.next = c_node.next.next
                return
            c_node = c_node.next
        
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
    
    wsk1 = lista1
    wsk2 = lista2
    suma = 0
    lista1 = lista1.next
    lista2 = lista2.next
    while (lista2!=None):
        val = lista2.val
        if wsk1.search(val)==False:
            wsk2.pop(val)
            suma += 1
        lista2 = lista2.next
    while (lista1!=None):
        val = lista1.val
        if wsk2.search(val)==False:
            wsk1.pop(val)
            suma += 1
        lista1 = lista1.next
    return suma


if __name__=="__main__":
    lista1 = Node()
    lista2 = Node()
    lista1.append(0); lista1.append(1); lista1.append(2); lista1.append(3); lista1.append(4); lista1.append(6)
    lista2.append(1); lista2.append(2); lista2.append(5); lista2.append(7); lista2.append(8)
    print(lista1)
    print(lista2)
    print(funk(lista1, lista2))
    print(lista1)
    print(lista2)
    