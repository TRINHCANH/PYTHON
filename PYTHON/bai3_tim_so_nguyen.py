print("chuong trinh tim so nguyen to")

#nhap vao so N , 1 toi 100 (hoan N)
N = int (input("nhap vao so nguyen di thang ngu: "))
#dung ong lap de tim so nguyen to  1 toi N
#kiem tra xem so do co phai la so nguyen to
# Neu so do chia het cho 1 va chinh no
# neu phai in ra man hinh
for n in range(2,N+1):
    so_nguyen = True
    for x in range(2, n):  
         if n % x == 0:
             so_nguyen = False
             break
    if so_nguyen == True:         
         print('%d' %n, end =' ')





