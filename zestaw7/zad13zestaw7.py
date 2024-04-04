class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        c_node = self
        if c_node.val==None:
            c_node.val = v
            return
        while (c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def __str__(self):
        c_node = self
        res = ""
        while(c_node!=None):
            if c_node.val!=None:
                res += str(c_node.val)+" "
            c_node = c_node.next
        return res

def rem(lista):
    
    negro = lista
    while (lista!=None and lista.next!=None):
        if lista.next.val<lista.val:
            lista.next = lista.next.next
        else:
            lista = lista.next
    return negro
    

if __name__=="__main__":
    lista = Node()
    lista.append(1); lista.append(1); lista.append(2); lista.append(3); lista.append(3); lista.append(1)
    print(lista)
    print(rem(lista))
    #1, 3
    