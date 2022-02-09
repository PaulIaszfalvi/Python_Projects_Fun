class LongestSubstring(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s)
        #set iterators to beginning of string
        # iter1 = 0
        # iter2 = 1
        # length = len(s)
        # mySet = set()
        # biggest_substring = 0

        # if length == 0 or length == 1: 
        #     pass
       
        # else:          
        #     mySet.add(s[iter1])            
        #     while iter2 < length :
               
        #         if s[iter2] in mySet:        
        #             iter1 += 1          
        #             while s[iter1] == s[iter2]:    
        #                 iter1 += 1   
        #             biggest_substring = max(biggest_substring, iter2-iter1)
                                     
                    
        #         else:                
        #             mySet.add(s[iter2])

        #         iter2 += 1    

        #     print(iter1, iter2)
        #     biggest_substring = max(biggest_substring, iter2-iter1)
      
        # return biggest_substring

        i1, i2, length, mySet = 0, 0, 0, set()

        while i2 < len(s): 
            
            if s[i2] not in mySet:
                mySet.add(s[i2])
                i2 += 1
            else:  
                mySet.remove(s[i1])
                i1 += 1
            length = max(length, i2 - i1)
        
        return length

        