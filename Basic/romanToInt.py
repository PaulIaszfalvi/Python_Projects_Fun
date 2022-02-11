from sqlalchemy import null


class RomanToInt(object):

    def convert(self, s):

        previous = 0
        head = 0
        total = 0

        values = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        print(s)

        for x in s[::-1]:
            temp = values.get(x)
            #Reset if value is greater than last one
            if previous < temp:
                head = 0
            #Set the head to check when the values are smaller we subtract   
            if temp >= head:
                head = temp
                total += head
            else:
                total -= temp
            previous = temp
            #print(x, temp)

        return total

