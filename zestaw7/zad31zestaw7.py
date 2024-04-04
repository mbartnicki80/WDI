class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def append(self, v):
        c_node = self
        while (c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def __str__(self):
        c_node = self
        res = ""
        while(c_node.next!=None):
            res += str(c_node.next.val)+" "
            c_node = c_node.next
        return res
    
    def pop(self, v):
        c_node = self
        while (c_node.next!=None):
            if c_node.next.val==v:
                c_node.next = c_node.next.next
                return
            c_node = c_node.next
    

def funk(lista1, lista2, lista3):
    
    suma = 0
    wsk = lista1
    lista1 = lista1.next
    while (lista1!=None):
        val = lista1.val
        if val%2==0 and val>0:
            lista2.append(val)
        elif val%2==1 and val<0:
            lista3.append(val)
        else: 
            wsk.pop(val)
            suma += 1
        lista1 = lista1.next
    return f"suma= {suma}"

if __name__=="__main__":
    lista1 = Node()
    lista2 = Node()
    lista3 = Node()
    lista1.append(2); lista1.append(3); lista1.append(10); lista1.append(-1); lista1.append(-2)
    print(lista1)
    print(funk(lista1, lista2, lista3))
    print(lista2)
    print(lista3)
    