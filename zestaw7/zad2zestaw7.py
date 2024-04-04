class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        if self.val==None:
            self.val = v
            return
        while(self.next!=None):
            self = self.next
        self.next = Node(v)
    
    def __str__(self):
        c_node = self
        res = ""
        while (c_node!=None):
            res += str(c_node.val)+" "
            c_node = c_node.next
        return res

def init(ele):
    lista = Node()
    for i in ele:
        lista.append(i)
    return lista

def search(lista, ind):
    i=0
    while(lista.next!=None and i!=ind):
        lista = lista.next
        i += 1
    if i==ind:
        return lista.val
    return "Nie ma takiego indeksu"

def change(lista, ind, v):
    i=0
    while(lista.next!=None and i!=ind):
        lista = lista.next
        i += 1
    if i==ind:
        lista.val = v
        return lista
    return "Nie ma takiego indeksu"

if __name__=="__main__":

    lista = init([1, 2, 3])
    lista.append(5); lista.append(7)
    print(lista)
    print(search(lista, 2))
    change(lista, 2, 10)
    print(lista)