class maxHeap:
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
        return get_left_child_index(i) < len(self.heap)

    def check_for_right_child(self, i):
        return get_right_child_index(i) < len(self.heap)

    def check_for_parent(self, i):
        return get_parent_index(i) >= 0

    def swap_elements(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def add_element(self, element):
        self.heap.append(element)
        self.find_sorted_position_in_heap_upwards(len(self.heap)-1)

    def find_sorted_position_in_heap_upwards(self, i):
        while (self.check_for_parent(i) and self.heap[i].get_priority() > self.heap[get_parent_index(i)].get_priority()):
            self.swap_elements(i, self.get_parent_index(i))
            i = self.get_parent_index(i)

    def find_sorted_position_in_heap_downwards(self, i):
        while(check_for_left_child(i)):
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
            leftChildIndex = get_left_child_index(i)
            if (self.check_for_right_child(i)):
                rightChildIndex = get_right_child_index(i)
                if (self.heap[leftChildIndex].get_priority() > self.heap[rightChildIndex].get_priority()):
                    return leftChildIndex
                else:
                    return rightChildIndex
        else:
            return -1

    def pop_root(self):
        if len(self.heap) == 0:
            return -1
        endOfList = len(self.heap) - 1
        self.swap_elements(0, endOfList)
        oldRoot = self.heap.pop()
        self.find_sorted_position_in_heap_downwards(0)
        return oldRoot

    def increment_priorities(self):
        for(element in self.heap):
            element.increment_priority()
        self.leaves = []
        get_leaf_nodes(0)
        for(leaf in self.leaves):
            find_sorted_position_in_heap_upwards(leaf)

    def get_leaf_nodes(self, i):
        if (check_for_left_child(i)!=True and check_for_right_child(i)!=True):
            self.leaves.append(i)
            return
        if (check_for_left_child(i)):
            get_leaf_nodes(get_left_child_index(i))
        if (check_for_right_child(i)):
            get_leaf_nodes(get_right_child_index(i))
