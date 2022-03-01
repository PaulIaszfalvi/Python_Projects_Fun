from scipy import rand


class ReverseRoman(object):
    def reverse(self, number):
        
        values = {
            1 : "I",
            5 : "V",
            10 : "X", 
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }

        return values.get(1000)