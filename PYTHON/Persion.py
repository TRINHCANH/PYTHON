class Person:

    __name =  ''
    __age : 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def run(self):
        print('toi la %s (%d tuoi), dang chay' % (self.__name,self.__age))

    def stop(self):
        print('toi la %s (%d tuoi), dung chay'% (self.__name,self.__age))

    def sing(self):
        print('toi la %s (%d tuoi), dang hat'% (self.__name,self.__age))

    def change_name(self, name):
        if (name == 'huy nguyen'):
            print('khong cho doi ten')
        else:
            self.__name = name



canh



