user_status = False

def login(func):

    def inner(*args):
        _username = "eric"
        _password = "123"
        global user_status

        if user_status == False:
            username = raw_input("user:")
            password = raw_input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            func(*args)

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


def japan():
    print("----japan----")


def henan():
    print("----henan----")




home()

america("back insert")