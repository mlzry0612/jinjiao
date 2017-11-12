import string

def initData():
    menu = {
        'Shanghai': {
            'pudong': '111',
            'puxi': '222'
        },
        'WuXi': {
            'wuxi1': ['ri','ji','ba'],
            'wuxi2': '2222'
        }
    }
    return menu


def readfile():
    with open('day2.txt', 'r') as ob1,  open('day3.txt', 'w') as write:
        for line in ob1:
            line = string.strip(line)
            if line != '':
                print line
                write.write(line+'love highheel\n')

if __name__ == '__main__':

    menu = initData()
    menu['cainia'] = 'sfsfs'
    value = menu.get('WuXi')
    wuxi1value = value.get('wuxi1')
    print wuxi1value
    wuxi1value.append('1')
    wuxi1value.insert(2,'sfsf')
    print wuxi1value


    array = ['1','2','3']
    array.insert(1,'322')
    array.append('234')
    array.append(['3','5'])  #append treat as list as one item
    array.extend(('2',))
    array.extend(['4','5','6']) #Extend put all item into  list
    print array.count('4')
    print array.index('3')
    print array.__len__()
    print array
    print value

    readfile()

