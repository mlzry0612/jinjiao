# -*- coding: utf-8 -*-

def hello():
    def hello1():
        print "hello"
    return hello1  #没有括号

a = hello()
a()