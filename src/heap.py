class MaxHeap:
    def __init__(self):
        self.heap = [] #Elements in the heap
        self.leaves = [] #Indecies to the leaf nodes in the heap

    def get_left_child_index(self, i):
        return (2*i)+1

    def get_right_child_index(self, i):
        return (2*i)+2

    def get_parent_index(self, i):
        return int((i-1)/2)

    def check_for_left_child(self, i):
        return self.get_left_child_index(i) < len(self.heap)

    def check_for_right_child(self, i):
        return self.get_right_child_index(i) < len(self.heap)

    def check_for_parent(self, i):
        return self.get_parent_index(i) >= 0

    def swap_elements(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def add_element(self, element):
        self.heap.append(element)
        self.find_sorted_position_in_heap_upwards(len(self.heap)-1)

    def find_sorted_position_in_heap_upwards(self, i):
        size = len(self.heap)
        if(i > 0):
            while (self.check_for_parent(i) and self.heap[i].get_priority() > self.heap[self.get_parent_index(i)].get_priority()):
                self.swap_elements(i, self.get_parent_index(i))
                i = self.get_parent_index(i)

    def find_sorted_position_in_heap_downwards(self, i):
        while(self.check_for_left_child(i)):
            maxChildIndex = self.get_max_child_index(i)
            if (maxChildIndex == -1):
                break
            if (self.heap[i].get_priority() < self.heap[maxChildIndex].get_priority()):
                self.swap_elements(i, maxChildIndex)
                i = maxChildIndex
            else:
                break

    def get_max_child_index(self, i):
        if (self.check_for_left_child(i)):
            leftChildIndex = self.get_left_child_index(i)
            if (self.check_for_right_child(i)):
                rightChildIndex = self.get_right_child_index(i)
                if (self.heap[leftChildIndex].get_priority() > self.heap[rightChildIndex].get_priority()):
                    return leftChildIndex
                else:
                    return rightChildIndex
            else:
                return leftChildIndex
        else:
            return int(-1)

    def pop_root(self):
        if len(self.heap) == 0:
            return -1
        endOfList = len(self.heap) - 1
        self.swap_elements(0, endOfList)
        oldRoot = self.heap.pop()
        self.find_sorted_position_in_heap_downwards(0)
        return oldRoot

    def increment_priorities(self):
        for element in self.heap:
            element.increment_priority()
        self.leaves = []
        self.get_leaf_nodes(0)
        for leaf in self.leaves:
            self.find_sorted_position_in_heap_upwards(leaf)

    def get_list(self):
        return self.heap

    def get_list_in_order(self):
        tempUnsorted = self.heap[:]
        tempSorted = []
        while(len(self.heap)>0):
            tempSorted.append(self.pop_root())
        self.heap = tempUnsorted
        return tempSorted

    def get_leaf_nodes(self, i):
        if (self.check_for_left_child(i)==False and self.check_for_right_child(i)==False):
            self.leaves.append(i)
            return
        if (self.check_for_left_child(i)):
            self.get_leaf_nodes(self.get_left_child_index(i))
        if (self.check_for_right_child(i)):
            self.get_leaf_nodes(self.get_right_child_index(i))
