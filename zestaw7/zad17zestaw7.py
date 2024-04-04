class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

    def append(self, v):
        c_node = self
        while (c_node.next!=None):
            c_node = c_node.next
        c_node.next = Node(v)
        c_node.next.prev = c_node

    def __str__(self):
        c_node = self
        res = ""
        while(c_node!=None):
            if c_node.val!=None:
                res += str(c_node.val)+" "
            c_node = c_node.next
        return res

def bin(ele):

    sum = [0]*2
    while ele!=0:
        sum[ele%2] += 1
        ele //= 2
    
    if sum[1]%2==1:
        return True
    return False
    

def rem(lista):
    
    wsk = lista
    while(lista.next!=None):
        if bin(lista.next.val):
            lista.next = lista.next.next
        else: 
            lista = lista.next

    return wsk
    

if __name__=="__main__":
    lista = Node()
    lista.append(2); lista.append(5); lista.append(1); lista.append(1); lista.append(2); lista.append(3); lista.append(3); lista.append(1)
    print(lista)
    print(rem(lista))
    