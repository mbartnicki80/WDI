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
    
    def len(self):
        c_node = self
        i = 0
        while (c_node.next!=None):
            i += 1
            c_node = c_node.next
        return i
    

def funk(lista1, lista2):
    wynik = Node()
    for i in range(max(lista1.len(), lista2.len())):
        wynik.append(0)
    wsk = wynik
    while (lista1.next!=None and lista2.next!=None):
        wynik.next.val = lista1.next.val - lista2.next.val
        wynik = wynik.next
        lista1 = lista1.next
        lista2 = lista2.next
    while (lista1.next!=None):
        wynik.next.val = lista1.next.val
        wynik = wynik.next
        lista1 = lista1.next
    while (lista2.next!=None):
        wynik.next.val = lista2.next.val*(-1)
        wynik = wynik.next
        lista1 = lista2.next
    return wsk

if __name__=="__main__":
    lista1 = Node()
    lista2 = Node()
    lista1.append(2); lista1.append(3); lista1.append(10); lista1.append(-1); lista1.append(-2)
    lista2.append(0); lista2.append(3); lista2.append(5); lista2.append(-1)
    print(lista1)
    print(lista2)
    print(funk(lista1, lista2))
    