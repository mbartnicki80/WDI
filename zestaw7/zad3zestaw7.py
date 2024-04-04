class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
    def append(self, v):
        c_node = self
        if c_node.val==None:
            c_node.val = v
            return
        while(c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def __str__(self):
        c_node = self
        res = ""
        while(c_node!=None):
            res += str(c_node.val)+" "
            c_node = c_node.next
        return res

def mergeit(lista1, lista2):
    lista = Node()
    while (lista1!=None and lista2!=None):
        if lista1.val < lista2.val:
            lista.append(lista1.val)
            lista1 = lista1.next
        else:
            lista.append(lista2.val)
            lista2 = lista2.next
    while (lista1!=None):
        lista.append(lista1.val)
        lista1 = lista1.next
    while (lista2!=None):
        lista.append(lista2.val)
        lista2 = lista2.next
    return lista

def mergerek(lista1, lista2, lista = Node()):
    if lista1==None and lista2==None:
        return lista

    if lista1!=None and lista2!=None:
        if lista1.val < lista2.val:
            lista.append(lista1.val)
            return mergerek(lista1.next, lista2, lista)
        else:
            lista.append(lista2.val)
            return mergerek(lista1, lista2.next, lista)

    if lista1!=None:
        lista.append(lista1.val)
        return mergerek(lista1.next, lista2, lista)

    if lista2!=None:
        lista.append(lista2.val)
        return mergerek(lista1, lista2.next, lista)

if __name__=="__main__":
    lista1 = Node()
    lista2 = Node()
    lista1.append(5); lista1.append(7); lista1.append(9)
    lista2.append(4); lista2.append(6); lista2.append(10)
    listait = mergeit(lista1, lista2)
    print(listait)
    listarek = mergerek(lista1, lista2)
    print(listarek)