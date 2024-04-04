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
            if c_node.val!=None:
                res += str(c_node.val)+" "
            c_node = c_node.next
            n += 1
        return res
    
    def search(self, v):
        c_node = self
        while (c_node.next!=None):
            if c_node.next.val==v:
                return True
            c_node = c_node.next
        return False

def funk(lista):
    
    nowa = Node()
    dl = 1
    while(lista.next!=None):
        if nowa.search(lista.next):
            wsk = lista.next
            lista = lista.next
            while (lista.next!=wsk):
                dl += 1
                lista = lista.next
            return dl
        nowa.append(lista.next)
        lista = lista.next

if __name__=="__main__":
    lista = Node()
    lista.append(0); lista.append(1); lista.append(2); lista.append(3); lista.append(4); lista.append(5); lista.append(6); lista.cykl(6)
    
    print(lista)
    print(funk(lista))
    