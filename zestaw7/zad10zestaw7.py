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
    
    def dodaj(self, lista):
        c_node = self
        while(c_node.next!=None):
            c_node=c_node.next
        c_node.next = lista

def sum(lista, lista1, lista2):

    if lista.next==None:
        lista2.val = (lista.val + lista1.val)%10
        return (lista.val + lista1.val)//10
    
    w = sum(lista.next, lista1.next, lista2.next)

    lista2.val = (lista.val + lista1.val + w)%10
    return (lista.val+lista1.val+w)//10

def dl(lista):
    l = 0
    while(lista!=None):
        l += 1
        lista = lista.next
    return l

def funk(lista1, lista2):

    lista3 = Node()         #lista3 - lista pomocnicza, zeby utworzyc nowa liste w stylu 0048 zamiast 48
    lista4 = Node()         #lista3 - lista z samymi zerami, w niej bedzie sumowanie
    len1 = dl(lista1)       #lista1 - 1 liczba
    len2 = dl(lista2)       #lista2 - 2 liczba

    for i in range(abs(len1-len2)):
        lista3.append(0)
    for i in range(max(len1, len2)):
        lista4.append(0)

    w = 0
    if len1<len2:
        lista3.dodaj(lista1)
        w = sum(lista2, lista3, lista4)
    else:
        lista3.dodaj(lista2)
        w = sum(lista1, lista3, lista4)

    if w==1:
        ltmp = Node(1)
        ltmp.next=lista4
        return ltmp
    return lista4
        
if __name__=="__main__":

    lista1 = Node()
    lista2 = Node()
    lista2.append(9); lista2.append(9); lista2.append(9)
    lista1.append(1)
    print(lista1)
    print(lista2)
    print(funk(lista1, lista2))