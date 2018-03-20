from libs.deque import Deque

def palchecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print("lsdkjfskf")
print(palchecker("lsdkjfskf"))
print("radar")
print(palchecker("radar"))
print("SOS")
print(palchecker("SOS"))
