class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def search(self, v):
        c_node = self
        while(c_node!=None):
            if c_node.val==v:
                return True
            c_node = c_node.next
        return False

    def append(self, v):
        c_node = self
        while(c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def pop_val(self, v):
        c_node = self
        while(c_node.next!=None and c_node.next.val!=v):
            c_node = c_node.next
        if c_node.next.val==v:
            c_node.next = c_node.next.next

    def __str__(self):
        res = ""
        c_node = self.next
        while(c_node!=None):
            res += str(c_node.val)+" "
            c_node = c_node.next
        return res

if __name__=="__main__":

    lista = Node(None)
    lista.append(5); lista.append(3); lista.append(4); lista.append(4)
    print(lista)
    lista.pop_val(4)
    lista.pop_val(4)
    lista.pop_val(5)
    print(lista)