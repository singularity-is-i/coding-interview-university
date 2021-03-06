from libs.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

print("Bill David Susan Jane Kent Brad - 7")
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))

print("Bill David Susan Jane Kent Brad - 9")
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],9))

