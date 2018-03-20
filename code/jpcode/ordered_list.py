from libs.ordered_list import OrderedList

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print("List Size:" , mylist.size())
print("Search 93:", mylist.search(93))
print("Search 100:", mylist.search(100))


