class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        c_node = self
        while(c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def pop_allval(self, v):
        c_node = self
        while (c_node.next!=None):
            if c_node.next.val == v:
                c_node.next = c_node.next.next
            else:
                c_node = c_node.next

    def __str__(self):
        c_node = self
        res = ""
        while (c_node.next!=None):
            res += str(c_node.next.val)+" "
            c_node = c_node.next
        return res

def rem(lista):
    while (lista!=None):
        lista.pop_allval(lista.val)
        lista = lista.next


if __name__=="__main__":
    lista = Node()
    lista.append(1); lista.append(1); lista.append(1); lista.append(2); lista.append(3); lista.append(3); lista.append(3)
    print(lista)
    rem(lista)
    print(lista)
