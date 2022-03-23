from Basic import fileReader
from Basic import randomNum
from Basic import bubbleSort
from Basic import binarySearch
from Basic import plusOne
from Basic import multiplyStrings
from Basic import longestSubstring
#from Basic import romanToInt
from Basic import reverseInteger
from Basic import reverseRomanToInt
from Basic import twoSum
# f = fileReader.FileReader()
# f.writeFile("personal_info.txt", "Hello World!")
# f.readFile("personal_info.txt")

# num = 10
# top = 1000
# name = "MyList"
# generateList = randomNum.RandomNum()
# list = generateList.getList(num, top)

# bSort = bubbleSort.BubbleSort()
# sorted_list = bSort.sort(list)

# search = binarySearch.BinarySearch()
# print(sorted_list)
# num = int(input("Enter a number preferably on the list: "))
# search.find(list, num)

# plus_one = plusOne.PlusOne();
# print(plus_one.plusOne([9,9,9]))

# ms = multiplyStrings.MultiplyStrings()
# print(ms.multiply("123", "55"))

# longest_substring = longestSubstring.LongestSubstring()
# print(longest_substring.lengthOfLongestSubstring("pwwkew"))

# romanInt = romanToInt.RomanToInt()
# print(romanInt.convert("MCMXXCIV")
# )

# reverseInt = reverseInteger.ReverseInteger()
# print(reverseInt.reverse(-12330))

# reverseRoman = reverseRomanToInt.ReverseRoman()
# print(reverseRoman.reverse("IV"))

sumTwo = twoSum.Solution()
print(sumTwo.twoSum( [2, 7, 11, 15], 9))
print(sumTwo.twoSum( [0, 4, 3, 0], 0))  
print(sumTwo.twoSum( [0, 4, 3, 0], 3))  
print(sumTwo.twoSum([2, 5, 6, 4, 3, 11, 7, 15], 9))