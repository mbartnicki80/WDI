class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        c_node = self
        res = ""
        while c_node!=None:
            res += str(c_node.val)+" "
            c_node = c_node.next
        return res
    
def append(lista, v):

        if lista.val == None:
            lista.val = v
            return
        while (lista.next!=None):
            lista = lista.next
        lista.next = Node(v)
        

if __name__=="__main__":

    lista = Node()
    append(lista, 2); append(lista, 5)
    print(lista)