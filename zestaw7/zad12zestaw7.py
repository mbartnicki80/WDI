class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        c_node = self
        res = ""
        while(c_node!=None):
            if c_node.val!=None:
                res += str(c_node.val)+" "
            c_node = c_node.next
        return res
    
    def moc(self):
        c_node = self
        i = 0
        while (c_node!=None):
            i += 1
            c_node = c_node.next
        return i
    
    def cont(self, v):
        c_node = self
        while(c_node!=None):
            if c_node.val==v:
                return True
            c_node = c_node.next
        return False

def append(lista, v):
    
    negro = lista
    if lista.cont(v)==0:
        if lista.val==None:
            lista.val = v
            print(negro)
            return True
        if lista.val>v:
            lista1 = Node(v)
            lista1.next = lista
            lista = lista1
            print(lista1)
            return True

        while lista.next!=None and lista.next.val<v:
            lista = lista.next
        lista.next, lista.next.next = Node(v), lista.next
        print(negro)
        return True
    print(lista)
    return False

if __name__=="__main__":
    lista = Node()
    print(append(lista, "str"))
    print(append(lista, "stra"))
    print(append(lista, "straj"))
    print(append(lista, "strajk"))
    print(append(lista, "strajk"))
    