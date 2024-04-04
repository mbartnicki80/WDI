class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def __str__(self):
        c_node = self
        res = ""
        n = 0
        while(c_node.next!=None and n<=15):
            res += str(c_node.next.val)+" "
            c_node = c_node.next
            n += 1
        return res

    def append(self, v):
        c_node = self
        while (c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def search(self, val):
        c_node = self
        while (c_node!=None):
            if c_node.val==val:
                return True
            c_node = c_node.next
        return False

    
def wstaw(lista, v):

        czy = Node()
        if lista.val==None:
            lista.val = v
            lista.next = lista
            return True
        while (True):
            if czy.search(lista):
                return False
            if v[0]>=lista.val[-1]:
                lista.next, lista.next.next = Node(v), lista.next
                return True
            czy.append(lista)
            lista = lista.next
        
if __name__=="__main__":
    lista = Node()
    print(wstaw(lista, "bartek")); print(wstaw(lista, "leszek")); print(wstaw(lista, "marek")); print(wstaw(lista, "ola")); print(wstaw(lista, "zosia"))
    print(lista)
    