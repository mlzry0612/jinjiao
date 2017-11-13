#coding=utf-8
user_status = False


def log(authlevel):

    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            if authlevel > 10:
                print ("LOGlOG")
                return func(*args, **kwargs)  #如果这里没有 return 那个这个fun 的 return 是不会返回东西给外面的  id()就为空
            else:
                print ("NO LOG NO lOG")
        return wrapper2

    return wrapper1  #NO () here


@log(20)
def home():
    print("----home----")


# need pass style into inner class, so need pass *args
@log(4)
def america(style):
    print("----america----"+style)
    return id(america)


def japan():
    print("----japan----")


def henan():
    print("----henan----")


home()

america("Back insert")