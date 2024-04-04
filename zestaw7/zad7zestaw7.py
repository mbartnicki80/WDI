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
        while c_node!=None:
            res += str(c_node.val)+" "
            c_node = c_node.next
        return res
    
def pop(lista):
    if lista.next==None:
        lista.val = None
        return
    while(lista.next.next!=None):
        lista = lista.next
    lista.next = None
    return
        
if __name__=="__main__":

    lista = Node()
    lista.append(12); lista.append(5)
    print(lista)
    pop(lista)
    print(lista)