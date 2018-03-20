def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print("[1,3,5,7,9]")
print(listsum([1,3,5,7,9]))


def listsum2(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum2(numList[1:])

print("[1,3,5,7,9]")
print(listsum2([1,3,5,7,9]))


