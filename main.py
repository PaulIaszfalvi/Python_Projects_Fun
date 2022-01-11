from Basic import fileReader
from Basic import randomNum
from Basic import bubbleSort
from Basic import binarySearch

# f = fileReader.FileReader()
# f.writeFile("personal_info.txt", "Hello World!")
# f.readFile("personal_info.txt")

num = 10
top = 1000
name = "MyList"
generateList = randomNum.RandomNum()
list = generateList.getList(num, top)

bSort = bubbleSort.BubbleSort()
sorted_list = bSort.sort(list)

search = binarySearch.BinarySearch()
print(sorted_list)
num = int(input("Enter a number preferably on the list: "))
search.find(list, num)
