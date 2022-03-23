from typing import List

from sklearn.utils import indexable

class Solution:

    def __init__(self) -> None:
        pass
        
    def twoSum(self, nums:List[int], target: int):

        numsMap = {}
        indexOfAnswers = []

        for i, n in enumerate(nums):

            complement = target - n
            
            if complement in numsMap:
                 indexOfAnswers.append(i)
                 indexOfAnswers.append(numsMap[complement])                
            numsMap[n] = i
        
        indexOfAnswers.sort()
        
        return set(indexOfAnswers)
        # complement = {}
        # indexes = []
        # count = 0

        # for number in nums:
        #     temp = target - number
        #     if  temp >= 0:
        #         complement.append(temp)
        
        # for index, n in enumerate(complement):

        #     print(index)
        #     if n in nums:
        #         indexes.append(nums.index(n))
        #         #(x for x in nums if x ==n[0])   
                
        #     count += 1

        # return indexes
   