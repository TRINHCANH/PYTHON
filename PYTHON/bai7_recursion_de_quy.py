print("chuong trinh diem danh dung phuong phap de quy ")

def diem_danh(n):
    if n == 1:
        return 1
    return diem_danh(n - 1) + 1

def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n - 1)

so_hoc_sinh = diem_danh(100)
print("so hoc sinh la: ", so_hoc_sinh)

n = int(input('nhap vao 1 so nguyen '))
so = factorial(n)
print(' %d! = %d ' %(n, so))