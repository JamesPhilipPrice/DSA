from heap import MaxHeap
from case import Case

class patientQueue:
    def __init__(self):
        self.caseDefinitions = {
        "LOC": ["Loss of Consciousness", 24, 6],
        "FOS": ["Fits or Seizures", 30, 7],
        "CP": ["Chest Pains", 42, 8],
        "BD": ["Breathing Difficulties", 60, 10],
        "SB": ["Severe Bleeding", 48, 10],
        "AR": ["Allergic Reactions", 12, 3],
        "BOS": ["Burns or Scalds", 18, 4],
        "S": ["Stroke", 36, 2],
        "RTA": ["Road Traffic Accident", 54, 5],
        "BA": ["Broken Arm", 6, 2]
        }
        self.menuOneText = "Please select one of the following options:\n(1):Add case\n(2):Retrieve next queued case\n(3):Quit program\n(4 (testing)): Increment time base priority\n(5): Print out entire list"
        self.addMenuText ="Please select one of the folloowing cases, or enter '-1' to return to the main menu"
        self.queue = MaxHeap()
        self.main_loop()

    def menu_one(self):
        print(self.menuOneText)
        validChoice = False
        while(not validChoice):
            choice = input(">>> ")
            if (choice in ["1", "2", "3", "4", "5"]):
                validChoice = True
            else:
                print("Invalid option, please re-enter...")
        return choice

    def add_menu(self):
        print(self.addMenuText)
        for key, value in self.caseDefinitions.items():
            print("Code: ", key, ", Name: ", value[0])
        validChoice = False
        while(not validChoice):
            choice = input(">>> ")
            if(choice in self.caseDefinitions):
                self.queue.add_element(Case(self.caseDefinitions[choice]))
                validChoice = True
            elif(choice == "-1"):
                validChoice = True
            else:
                print("Invalid option, please re-enter...")
        return choice

    def main_loop(self):
        while (True):
            menuOneChoice = self.menu_one()
            if(menuOneChoice == "1"):
                if(self.add_menu() == "-1"):
                    continue
                else:
                    print(self.queue.get_list())
                    continue
            elif(menuOneChoice == "2"):
                print(self.queue.pop_root())
                continue
            elif(menuOneChoice == "3"):
                break
            elif(menuOneChoice == "5"):
                print("_"*20)
                for case in self.queue.get_list_in_order():
                    print(case.description, ":", case.get_priority())
                continue
            self.queue.increment_priorities()


PQ = patientQueue()
