import random 

class RandomNum:
    def __init__(self) -> None:
        self.nothing = 0

    def getList(self, n, top):
        list = []

        for i in range(0,n):
            list.append(random.randint(0, top))

        return list