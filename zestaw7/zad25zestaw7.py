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

    def cykl(self, ind):
        c_node = self
        i = 0
        wsk = None
        while (c_node.next!=None):
            if i == ind:
                wsk = c_node
            c_node = c_node.next
            i += 1
        if wsk==None:
            wsk = c_node
        c_node.next = wsk

    def __str__(self):
        c_node = self
        res = ""
        n = 0
        while(c_node!=None and n<20):
            res += str(c_node.val)+" "
            c_node = c_node.next
            n += 1
        return res
    
    def search(self, v):
        c_node = self
        while (c_node!=None):
            if c_node.val==v:
                return True
            c_node = c_node.next
        return False

def funk(lista):
    
    nowa = Node()
    dl = 0
    while(lista.next!=None):
        if nowa.search(lista):
            wsk = lista
            lista = lista.next
            dlcykl = 1
            while (lista!=wsk):
                dlcykl += 1
                lista = lista.next
            return dl-dlcykl
        nowa.append(lista)
        lista = lista.next
        dl += 1
    
def szukaj(lista, dlugosc):
    while dlugosc>1:
        lista = lista.next
        dlugosc -= 1
    return lista

if __name__=="__main__":
    lista = Node()
    lista.append(0); lista.append(1); lista.append(2); lista.append(3); lista.append(4); lista.append(5); lista.append(6); lista.cykl(5)
    
    print(lista)
    dlugosc = funk(lista)
    print(szukaj(lista, dlugosc).val)