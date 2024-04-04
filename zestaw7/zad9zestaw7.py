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

def funk(lista, ind=0):
    if lista.next==None:
        lista.val = (lista.val+1)%10
        return
            
    funk(lista.next, ind+1)
    if lista.next.val == 0:
        lista.val = (lista.val+1)%10
    
    if ind==0 and lista.val==0:
        lista1 = Node(1)
        while (lista!=None):
            lista1.append(lista.val)
            lista = lista.next
        return lista1

    return lista
    
if __name__=="__main__":

    lista = Node()
    lista.append(9); lista.append(9); lista.append(9)
    print(lista)
    print(funk(lista))