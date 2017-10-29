def itertest():
    a = [1,2,3,4,5,6]
    for i in a:
        print (i)

    for i, w in enumerate(a):
        print(i)

def yieldtest(amount):
    print amount
    while amount > 0:
        amount -=1
        print amount
        yield amount * 3


import time


def func(n):
    for i in range(0, n):
        arg = yield i
        print('func:', arg)


if __name__ == '__main__':
    itertest()
    print "======================"
    for  i in yieldtest(10):
        print i

    print "======================"
    fu = func(5)
    fu.send(None)
    while True:
        print ("main:", fu.send(200))


