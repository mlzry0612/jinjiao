__author__ = 'liama'

import getpass


def entirename():
    count = 0
    while(count < 3):
        user_name = raw_input("please input the name:")
        passwd = getpass.getpass("please entire the pwd:")
        if user_name.lower() == "eric" and passwd.lower() == "highheel":
            print "login correct"
            return
        else:
            print "login failed"
        count += 1
    else:
        print("sb")


if __name__ == '__main__':
    entirename()
