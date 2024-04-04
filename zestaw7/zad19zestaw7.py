class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        c_node = self
        while(c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def ile(self, v):
        i = 0
        while(self!=None):
            if self.val>v:
                return i
            if self.val==v:
                i += 1
            self = self.next
        return i

    def pop_allval(self, v):
        c_node = self
        i = 0
        while (c_node.next!=None):
            if c_node.next.val > v:
                break
            if c_node.next.val == v:
                c_node.next = c_node.next.next
                i += 1
            else:
                c_node = c_node.next
        return i

    def __str__(self):
        c_node = self
        res = ""
        while (c_node.next!=None):
            res += str(c_node.next.val)+" "
            c_node = c_node.next
        return res

def rem(lista):
    suma = 0
    while (lista!=None and lista.next!=None):
        if lista.next.ile(lista.next.val)>1:
            suma += lista.pop_allval(lista.next.val)
        lista = lista.next
    return suma


if __name__=="__main__":
    lista = Node()
    lista.append(1); lista.append(1); lista.append(1); lista.append(2); lista.append(3); lista.append(3); lista.append(3)
    print(lista)
    print(rem(lista))
    print(lista)
