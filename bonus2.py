
from lib.queue import Queue

class MinHeap() :

    def __init__(self) :
        pass
        
    def build_heap(self, keys) :
        self.var = []
        self.tree = []
        self.power = 0
        self.length = len(keys)
        while self.length > 1 :
            self.length = self.length // 2
            self.power = self.power + 1
            # print (self.length)

        for i in range (0, self.power+1) :
            if 2 ** i < 2 ** self.power :
                for j in range (0, 2 ** i) :
                    self.var.append(keys[2 ** i + j - 1])
                self.tree.append(self.var)
                self.var = []
            elif 2 ** i >= 2 ** self.power :
                for j in range (0, len(keys) - 2 ** self.power + 1):
                    self.var.append(keys[2 ** i + j - 1])
                self.tree.append(self.var)
        
        
        return self.tree

    def insert (self, item) :
        # print (self.power)
        # print (self.tree)
        # print (len(self.tree[self.power]))
        if len(self.tree[self.power]) == 2 ** self.power :
            self.tree.append([])
            self.tree[self.power + 1].append(item)
        elif len(self.tree[self.power]) < 2 ** self.power :
            self.tree[self.power].append(item)
        return self.tree

    def initialize (self) :
        
        q = Queue()
        
        for i in range (self.power, 0, -1) :
            for j in range (0, 2 ** (i-1)) :
                # for k in range (1, i + 1) :
                # if self.tree[i][2 * j] < self.tree[i-1][j] :
                #     q.enqueue(self.tree[i][2 * j])
                #     q.enqueue(self.tree[i-1][j])
                #     self.tree[i-1].insert(j, q.dequeue())
                #     self.tree[i][2 * j].insert(2 * j, q.dequeue())
                    # try :
                    #     self.tree[i][2 * j]
                    #     self.tree[i - k][j]
                    # except IndexError :
                    #     break
                    # else :
                    #     if self.tree[i][2 * j] < self.tree[i - k][j] :
                    #         q.enqueue(self.tree[i][2 * j])
                    #         del self.tree[i][2 * j]
                    #         q.enqueue(self.tree[i - k][j])
                    #         del self.tree[i - k][j]
                    #         self.tree[i - k].insert(j, q.dequeue())
                    #         self.tree[i].insert(2 * j, q.dequeue())
                    #     else :
                    #         pass
                    try :
                        self.tree[i][2*j+1]
                        self.tree[i-1][j]
                    except IndexError :
                        try :
                            self.tree[i][2*j]
                            self.tree[i-1][j]
                        except IndexError :
                            continue
                        else :
                            if self.tree[i][2*j] < self.tree[i-1][j] :
                                q.enqueue(self.tree[i][2*j])
                                del self.tree[i][2*j]
                                q.enqueue(self.tree[i-1][j])
                                del self.tree[i-1][j]
                                self.tree[i-1].insert(j, q.dequeue())
                                self.tree[i].insert(2*j, q.dequeue())
                    else :
                        for k in range (0, self.power-i+1) :
                            try :
                                self.tree[i+k][2*j+1]
                            except IndexError :
                                try :
                                    self.tree[i+k][2*j]
                                except IndexError :
                                    break
                                else :
                                    if self.tree[i+k][2*j] < self.tree[i+k-1][j] :
                                        q.enqueue(self.tree[i+k][2*j])
                                        del self.tree[i+k][2*j]
                                        q.enqueue(self.tree[i+k-1][j])
                                        del self.tree[i+k-1][j]
                                        self.tree[i+k-1].insert(j, q.dequeue())
                                        self.tree[i+k].insert(2*j, q.dequeue())
                            else :
                                if self.tree[i+k][2*j+1] < self.tree[i+k-1][j] and self.tree[i][2*j+1] < self.tree[i][2*j] :
                                    q.enqueue(self.tree[i+k][2*j+1])
                                    del self.tree[i+k][2*j+1]
                                    q.enqueue(self.tree[i+k-1][j])
                                    del self.tree[i+k-1][j]
                                    self.tree[i+k-1].insert(j, q.dequeue())
                                    self.tree[i+k].insert(2*j+1, q.dequeue())
                                    j = 2*j+1
                                elif self.tree[i+k][2*j] < self.tree[i+k-1][j] :
                                    q.enqueue(self.tree[i+k][2*j])
                                    del self.tree[i+k][2*j]
                                    q.enqueue(self.tree[i+k-1][j])
                                    del self.tree[i+k-1][j]
                                    self.tree[i+k-1].insert(j, q.dequeue())
                                    self.tree[i+k].insert(2*j, q.dequeue())
                                    j = 2*j


                        #     for k in range (i ,self.power) :
                        #         if self.tree[i+1][2*(2*j+1)] < self.tree[i][2*j+1] :

                        # else :
                        #     for k in range (i, i+self.power) :
        return self.tree

    def del_min (self) :

        q = Queue()

        # q.enqueue(self.tree[0][0])
        del self.tree[0][0]
        # print (self.tree[self.power][len(self.tree[self.power])-1])
        q.enqueue(self.tree[self.power][len(self.tree[self.power])-1])
        del self.tree[self.power][len(self.tree[self.power])-1]
        # self.tree[self.power].insert(len(self.tree[self.power]), q.dequeue())
        self.tree[0].insert(0, q.dequeue())
        return self.tree
    
    def display (self) :
        print (self.tree)


heap = MinHeap()
heap.build_heap([25, 90, 26, 7, 19, 17, 1, 2])
heap.initialize()
heap.display()

heap.insert(1)
heap.initialize()
heap.display()

heap.insert(7)
heap.initialize()
heap.display()

heap.del_min()
heap.initialize()
heap.display()

# li = []
# for l in range (1, 15) :
#     li.append(l)
# heap.build_heap(li))


# print (x.build_heap([5, 14, 23, 12, 26, 34, 20, 24, 35]))
