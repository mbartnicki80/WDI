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
        n = 0
        while(c_node!=None and n<20):
            res += str(c_node.val)+" "
            c_node = c_node.next
            n += 1
        return res
    
    def search(self, lista):
        c_node = self
        while (c_node!=None):
            if lista==None:
                return True
            if c_node.val==lista.val:
                lista = lista.next
            c_node = c_node.next
        if lista==None:
            return True
        return False

def funk(lista1, lista2):
    
    if lista1.search(lista2) or lista2.search(lista1):
        return True
    return False

if __name__=="__main__":
    lista1 = Node()
    lista2 = Node()
    lista1.append(0); lista1.append(1); lista1.append(2); lista1.append(3); lista1.append(4); lista1.append(5); lista1.append(6)
    lista2.append(1); lista2.append(2); lista2.append(6)
    print(lista1)
    print(lista2)
    print(funk(lista1, lista2))
    