class ReverseInteger(object):

    def __init__(self) -> None:
        pass

    def checkInt(self, newInt):

        print()
        if -2**31 < newInt < 2**31-1:
            return newInt
        else:
            return 0

    def reverse(self, x):

        sign = 1

        if x < 0:
            sign = -1
            x = abs(x)

        s = str(x)
        #print(x, s, int(s[::-1]) if x > 0 else -1*int(s[:0:-1]))
        
        return self.checkInt(sign * int(s[::-1]))
     

   
