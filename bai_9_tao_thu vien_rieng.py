# print("viet chuong trinh thu vien rieng ")
# class Mylib:
#     def add(self,x,y):
#         print ("")

class Comedian:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        # return f"{self.first_name} {self.last_name} is {self.age}."
        print('toi la %s %s(%d tuoi), dang chay' % (self.first_name,self.last_name,self.age))

    def repr(self):
        print('toi la %s %s(%d tuoi), dang chay canh' % (self.first_name,self.last_name,self.age))


canh = Comedian('nguyen','huy',30)
canh.__str__()
canh.repr()
