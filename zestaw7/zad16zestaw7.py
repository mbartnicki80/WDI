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
        while(c_node!=None):
            if c_node.val!=None:
                res += str(c_node.val)+" "
            c_node = c_node.next
        return res

def osem(ele):

    sum = [0]*8
    while ele!=0:
        sum[ele%8] += 1
        ele //= 8
    
    if sum[5]%2==0:
        return True
    return False
    

def rem(lista):
    
    nowalista = Node()
    nowalista2 = Node()
    wsk = nowalista

    while(lista!=None and lista.next!=None):
        if osem(lista.next.val):
            nowalista.append(lista.next.val)
        else: 
            nowalista2.append(lista.next.val)
        lista = lista.next

    print(nowalista)
    while (nowalista.next!=None):
        nowalista = nowalista.next
    nowalista.next = nowalista2

    return wsk
    

if __name__=="__main__":
    lista = Node()
    lista.append(2); lista.append(5); lista.append(1); lista.append(1); lista.append(2); lista.append(3); lista.append(3); lista.append(1)
    print(lista)
    print(rem(lista))
    