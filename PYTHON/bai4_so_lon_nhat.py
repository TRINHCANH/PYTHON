import random

print("chuong trinh tim so lon nhat trong danh sach!")
#vong lap chay tu 0 toi N toa tau
#neu so trong toa tau > so largest thi 
danh_sach = []

for n in range (10):
    danh_sach.append(random.randrange(100, 1000))
    print('%d ' %danh_sach[n], end = ' ') 

vi_tri = 0 
so_max = danh_sach[vi_tri]
# print('so_max: %d tai vi tri: %d ' %(so_max,vi_tri))
for n in range(len(danh_sach)):
     if danh_sach[n] > so_max:
         so_max = danh_sach[n]
         vi_tri = n

print('')
print('so lon nhat: %d' %so_max)
print('tai vi tri: %d' %vi_tri)       