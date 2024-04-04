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
    
def pop2(lista):

    while(lista!=None and lista.next!=None):
        lista.next = lista.next.next
        lista = lista.next

        
if __name__=="__main__":

    lista = Node()
    lista.append(12); lista.append(5); lista.append(51); lista.append(6); lista.append(7); lista.append(2); lista.append(12); lista.append(66)
    print(lista)
    pop2(lista)
    print(lista)