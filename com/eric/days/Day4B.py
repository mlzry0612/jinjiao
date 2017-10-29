user_status = False

#Put func into func

def login(func):
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
        func()


def home():
    print("---home----")


def america():
    print("----america----")


def japan():
    print("----japan----")


def henan():
    print("----henan----")


home()
login(america)
# home()
# america()
login(henan)