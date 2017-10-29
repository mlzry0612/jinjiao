import time
import datetime
import random


if __name__ == '__main__':
    print (time.time())
    print (time.clock())
    print (time.clock())



    print (datetime.datetime.now())
    print(datetime.date.fromtimestamp(time.time()))
    print(datetime.datetime.now() + datetime.timedelta(3))

    print random.random()
    print random.randint(1, 200)
    print random.randrange(1, 10)
