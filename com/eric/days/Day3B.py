# -*- coding: utf-8 -*-

#闭包
def hello():
    def hello1():
        print "hello"
    return hello1  #没有括号

a = hello()
a()



#典型的闭包操作

def test1(x):
    def test2(y):
        print(x + y)
    return test2

#10保存在内存中,  非常像 java 的内部类, test2可以得到全部的变量的值
obj = test1(10)
obj(20)

