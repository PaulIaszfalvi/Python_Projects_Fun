class BubbleSort:

    def __init__(self) -> None:
        self.nothing = 0
    
    def sort(self, list):

        length = len(list)
        swap = 0

        for i in range(length-1):

            swap = 0

            for j in range(0, length-i-1):
               
                if list[j] > list[j+1]:
                    #temp = list[j]
                    #list[j] = list[j+1]
                    #list[j+1] = temp
                    list[j], list[j+1] = list[j+1], list[j]
                    swap += 1

            #print("Swap #" + str(i) + " : ")
            #print(list)
            if swap == 0:
                break

        return list