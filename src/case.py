class Case:
    def __init__(self, details):
        self.description = details[0]
        self.__priority = details[1]
        self.__incrementAmount = details[2]

    def get_priority(self):
        return self.__priority

    def increment_priority(self):
        self.__priority += self.__incrementAmount
