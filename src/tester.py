import matplotlib.pyplot as plt
import heap, case, time
class Tester:
    def __init__(self):
        plt.style.use('fivethirtyeight')
        self.add_test(40000, 10)

    def add_loop(self, i):
        arr = []
        self.queue = heap.MaxHeap()
        for x in range(i):
            temp = case.Case(["null", x+1, 0])
            self.queue.add_element(temp)
        return self.queue

    def single_run_add(self, i):
        startTime = time.perf_counter()
        self.add_loop(i)
        print(time.perf_counter()-startTime)

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

    def add_test(self, i, t):
        averages = []
        tempList = []
        xAxis = [n for n in range(0, i+1000, 1000)]
        
        print("running base test")
        for x in range(0, i+1000, 1000):
            startTime = time.perf_counter()
            self.add_loop(x)
            averages.append(time.perf_counter() - startTime)
        for test in range(1, t):
            tempList = []
            for x in range(0, i+1000, 1000):
                startTime = time.perf_counter()
                self.add_loop(x)
                tempList.append(time.perf_counter() - startTime)
            for x in range(len(averages)):
                averages[x] += tempList[x]
                averages[x] = averages[x] / 2
        print(averages)
        plt.plot(xAxis, averages)
        ##plt.tight_layout()
        plt.show()
        
t = Tester()
