class PlusOne(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        length = len(digits) -1
        #Carry doesnt matter        
        carry = 0

        while(length >= 0):
            print(digits[length], length)
            #We get a value of 10 if we add one
            if digits[length] == 9:
                digits[length] = 0               
                carry = 1
                length -= 1
                #Add to front of list if list ends
                if length < 0:
                    digits = [1] + digits
                    break
                pass
          
            #We get a value less than 10, so we just add
            if digits[length] < 9:
                digits[length] += 1
              
                if length < 0:
                    digits = [1] + digits
                    break
                break

            if carry == 0:
                length -= 1
            # if digits[length] == 9 and carry == 1:
            #     digits[length] = 0
                
            #     if length == 0:
            #         digits = "".join([1], digits)
                

           

            
        # for num in digits[::-1]:
        #     num += 1
        #     print(num)
        #     break

        return digits
