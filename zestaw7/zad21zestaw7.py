class Node:
    def __init__(self, v=None):
        self.val = v
        self.next = None

    def append(self, v):
        c_node = self
        while(c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)

    def pop_ind(self, pocz, kon):
        c_node = self
        i = 0
        while (i<=kon):
            if pocz<=i<=kon:
                c_node.next = c_node.next.next
            else:
                c_node = c_node.next
            i += 1

    def __str__(self):
        c_node = self
        res = ""
        while (c_node.next!=None):
            res += str(c_node.next.val)+" "
            c_node = c_node.next
        return res

def rem(lista):

    maxdl = 1; maxpocz = -1; ilosc = 1
    ind = 0
    wsk = lista
    lista = lista.next
    while (lista!=None and lista.next!=None):
        pom = lista.next

        if (lista.next.val>lista.val):
            pocz = ind
            dl = 1
            while (lista.next!=None and lista.next.val>lista.val):
                dl += 1
                if maxdl==dl:
                    ilosc += 1
                if dl>maxdl:
                    ilosc = 1
                    maxdl = dl
                    maxpocz = pocz

                lista = lista.next
                ind += 1
        else:
            lista = lista.next
            ind += 1
    
    if ilosc==1:
        wsk.pop_ind(maxpocz, maxpocz+maxdl-1)



if __name__=="__main__":
    lista = Node()
    lista.append(15); lista.append(2); lista.append(7); lista.append(8); lista.append(9); lista.append(5); lista.append(13)
    print(lista)
    rem(lista)
    print(lista)
