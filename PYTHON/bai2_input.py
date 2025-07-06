# print("hello")
# #input
name = input('nhap vao ten cua ban: ')
age = int(input("ban bao nhieu tuoi: "))
print('cach1: chao ban %s,ban %d tuoi ha?, nam sau ban %d tuoi'%(name, age, age +1))
print('cach2: chao ban {0},ban {1} tuoi ha ?'.format(name,age))
print('')
print('canh')

#tinh dien tich va chu vi hinh chu nhat
# nhap chieu dai chieu rong tu banphim
width = int (input('nhap vao chieu rong: '))
length = int (input ('nhap cao chieu dai: '))
#tinh dien tich = dai * rong
dien_tich = length * width
#tinh chu vi =  (dai + rong)* 2
chu_vi =  (length + width) * 2
#in ra man hinh
print('chieu dai cua hinh chu nhat la {0}'.format(length))
print('chieu rong cua hinh chu nhat la {0}'.format(width))
print('dien tich cua hinh chu nhat la {0}'.format(dien_tich))
print('chu vi cua hinh chu nhat la {0}'.format(chu_vi))

name =  ''