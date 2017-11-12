# -*- coding: utf-8 -*-
import string

def setcompart():
    a = {1,2,3,4}
    b = {3,4,5,6}
    difference = a.symmetric_difference(b)
    print ("symmetric_difference is %s" % difference)

    union = a.union(b)
    print ("union is %s" % union)

    a_difference = a.difference(b)
    print ("a_difference is %s" % a_difference)

    print a & b
    print a | b
    print a - b


def printparamers(name, age='30', favriote='HIGHHEEL'):
    print (name, age, favriote)


def stu_register(name,age,*args):   # * args is
    print(name,age,args)

def double_start(name, age, ** args): # ** args is dict
    print (name, age, args)



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



#ython 不允许overload  后面的会覆盖前面的

def star(x,y):
    print x

def star(x, y, z):
    print x, y, z





if __name__ == '__main__':
    setcompart()
    printparamers('Eric','20')
    printparamers('Lucy')
    stu_register('Eric',20, 'HIGH', "HEEL")
    stu_register('2eri',22)

    print int(4/2)

    data = [1, 3]
    midsplit(data, 1)

    double_start('Eric', '20', c=80, ss=90)

    x = [1,2,3] #Da San value into star function  d 在

    # * 将参数打菜成位置参数做为传递， 类似于一个list
    # ** 将参数打散成成字典

    star(*x)

    y = {'x':1, 'y':2, 'z':23}
    star(**y)

    str = "abc"

    print id(y)


#Python 默认是引用传递
#通过 list(t)消除强引用, 可以通过 ID 来看引用
