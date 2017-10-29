import string

def setcompart():
    a = {1,2,3,4}
    b = {3,4,5,6}
    difference = a.symmetric_difference(b)
    print difference

    union = a.union(b)
    print union

    a_difference = a.difference(b)
    print a_difference

    print a & b
    print a | b
    print a - b

def printparamers(name, age='30', favriote='HIGHHEEL'):
    print (name, age, favriote)


def stu_register(name,age,*args):
    print(name,age,args)

time = 0
def midsplit(data, number):
    global time
    time += 1
    print ("time is %s" % time)
    if len(data) > 1:
        mid = int(len(data)/2)
        print ("mid number is %d" % data[mid])
        if data[mid] == number:
            print "Got it"
        elif number < data[mid]:
            midsplit(data[:mid], number)
        elif number > data[mid]:
            midsplit(data[mid:], number)
    elif data[0] == number:
        print "Got it"
    else:
        print "Can't find it"


if __name__ == '__main__':
    setcompart()
    printparamers('Eric','20')
    printparamers('Lucy')
    stu_register('Eric',20, 'HIGH', "HEEL")

    print int(4/2)

    data = [1, 3]
    midsplit(data, 1)