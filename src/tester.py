import matplotlib.pyplot as plt
import heap, case, time
class Tester:
    def __init__(self):
        plt.style.use('fivethirtyeight')
        self.add_test(1000)

    def add_loop(self, i):
        arr = []
        self.queue = heap.MaxHeap()
        for x in range(i):
            temp = case.Case(["null", x+1, 0])
            self.queue.add_element(temp)
        return self.queue

    def pop_test(self, i):
        testOne = []
        testTwo = []
        testThree = []
        averages = []
        xAxis = [n for n in range(0, i+10, 10)]
        print("Running test 1")
        for x in range(0, i+10, 10):
            queue = self.add_loop(x)
            startTime = time.perf_counter()
            while(len(queue.heap) > 0):
                queue.pop_root()
            testOne.append(time.perf_counter() - startTime)
        print("Running test 2")
        for x in range(0, i+10, 10):
            queue = self.add_loop(x)
            startTime = time.perf_counter()
            while(len(queue.heap) > 0):
                queue.pop_root()
            testTwo.append(time.perf_counter() - startTime)
        print("Running test 3")
        for x in range(0, i+10, 10):
            queue = self.add_loop(x)
            startTime = time.perf_counter()
            while(len(queue.heap) > 0):
                queue.pop_root()
            testThree.append(time.perf_counter() - startTime)
        for x in range(len(testOne)):
            averages.append((testOne[x]+testTwo[x]+testThree[x])/3)
        plt.plot(xAxis, averages)
        ##plt.tight_layout()
        plt.show()

    def add_test(self, i):
        testOne = []
        testTwo = []
        testThree = []
        averages = []
        xAxis = [n for n in range(0, i+10, 10)]
        print("running test one")
        for x in range(0, i+10, 10):
            startTime = time.perf_counter()
            self.add_loop(x)
            testOne.append(time.perf_counter() - startTime)
        print("running test two")
        for x in range(0, i+10, 10):
            startTime = time.perf_counter()
            self.add_loop(x)
            testTwo.append(time.perf_counter() - startTime)
        print("running test three")
        for x in range(0, i+10, 10):
            startTime = time.perf_counter()
            self.add_loop(x)
            testThree.append(time.perf_counter() - startTime)
        for x in range(len(testOne)):
            averages.append((testOne[x]+testTwo[x]+testThree[x])/3)
        plt.plot(xAxis, averages)
        ##plt.tight_layout()
        plt.show()
        
t = Tester()
