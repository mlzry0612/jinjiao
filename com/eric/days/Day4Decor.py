#coding=utf-8
user_status = False


def login(func):

    def inner(*args):
        _username = "eric"
        _password = "123"
        global user_status

        print type
        if user_status == False:
            username = raw_input("user:")
            password = raw_input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            return func(*args)  #如果这里没有 return 那个这个fun 的 return 是不会返回东西给外面的  id()就为空

    return inner  #NO () here


def login2(func):
    def inner():
        print ("THIS is 222222")
        func()
    return  inner  #NO () here


@login2
def home():
    print("----home----")


# need pass style into inner class, so need pass *args
@login
def america(style):
    print("----america----"+style)
    return id(america)


def japan():
    print("----japan----")


def henan():
    print("----henan----")




home()

s = america("back insert")
print s