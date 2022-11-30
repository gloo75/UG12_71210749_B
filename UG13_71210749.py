class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.child = []

class Tree:
    def __init__(self,root):
        self.root = root

    def addChild(self, node_parent,data):
        node_baru = Node(data)
        node_baru.parent = node_parent
        node_parent.child.append(node_baru)
        return node_baru 
        
        #tulis kode Anda di sini
        #1. buat node baru menggunakan Class Node()
        #2. isi parent dari node baru tersebut dengan node_parent
        #3. node_parent menambahkan node baru (anaknya)
        #4. return node baru
        pass

    def sums(self,node):
        sum = 0
        if len(node.child) == 0:
            return node.data
        for anak in node.child:
            sum += self.sums(anak)
        return sum + node.data
        #tulis kode Anda di sini
        pass
                
    def sibling(self,node):
        if len(node.parent.child) == 0:
            return node._data
        elif len(node.parent.child) == 1:
            return node.data
        else:
            saudara = 0
            for anak in node.parent.child:
                saudara += anak.data
            return saudara
        #tulis kode Anda di sini
        pass
    

if __name__ =='__main__':
    val200 = Node(200)
    t = Tree(val200)

    val23 = t.addChild(val200, 23) 
    val11 = t.addChild(val200, 11)

    val13 = t.addChild(val23, 13) 
    val57 = t.addChild(val23, 57) 

    val32 = t.addChild(val11, 32) 

    val42 = t.addChild(val13, 42) 
    val51 = t.addChild(val13, 51) 
    val71 = t.addChild(val13, 71) 

    val12 = t.addChild(val57, 12) 
    val15 = t.addChild(val57, 15)

    val33 = t.addChild(val32, 33)
    val8 = t.addChild(val32, 8)

    print(f'Total value of node {val200.data} and all of its decendands = {t.sums(val200)}')
    print(f'Total value of all sibling on node {val33.data} = {t.sibling(val33)}')