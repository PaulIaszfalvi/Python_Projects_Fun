import time

class BinarySearch: 

    def find(self, list, num):
        
        left = 0
        right = len(list) 
        notFound = True

        while left < right:

            mid = int((right+left)/2)

            if num == list[mid]:
                print("Found your number at: " + str(mid))
                notFound = False
                break
            elif num < list[mid]:
                right = mid-1
            elif num > list[mid]:
                left = mid+1
            else:
                break
            # print("Right: " + str(right))
            # print("Left: " + str(left))
            # print("Looking at number: " + str(list[mid]))
            # time.sleep(0.25)
        if notFound:
            print("Sorry, your number wasn't there.")