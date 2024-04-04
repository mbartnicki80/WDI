class Node:
    def __init__(self, val1=None, val2=None):
        self.val1 = val1
        self.val2 = val2
        self.next = None

    def append(self, v1, v2):
        c_node = self
        while(c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v1, v2)

    def pop_val(self, v1, v2):
        c_node = self
        while (c_node.next!=None):
            if c_node.next.val1 == v1 and c_node.next.val2 == v2:
                c_node.next = c_node.next.next
                return
            else:
                c_node = c_node.next

    def __str__(self):
        c_node = self
        res = ""
        while (c_node!=None):
            if c_node.val1 != None and c_node.val2 != None:
                res += "["+str(c_node.val1)+", "+str(c_node.val2)+"] "
            c_node = c_node.next
        return res

def rem(lista):

    while (lista.next!=None):
        wsk = lista.next.next
        while (wsk!=None):
            if not (wsk.val2<lista.next.val1 or wsk.val1>lista.next.val2):
                lista.next.val1 = min(wsk.val1, lista.next.val1)
                lista.next.val2 = max(wsk.val2, lista.next.val2)
                lista.pop_val(wsk.val1, wsk.val2)
            wsk = wsk.next

        lista = lista.next



if __name__=="__main__":
    lista = Node()
    lista.append(15,19); lista.append(2,5); lista.append(7,11); lista.append(8,12); lista.append(5,6); lista.append(13,17)
    print(lista)
    rem(lista)
    print(lista)
