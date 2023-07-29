def so_nguyen(n):
    yes = True
    for x in range(2, n):  
         if n % x == 0:
             yes = False
             break
    return yes


N = int(input('nhap vao so nguyen to di ban: '))
for n in range(2, N+1):
    if so_nguyen(n):
        print('%d' % n, end =' ')

print('')
y = lambda a: a * 5
print (y(10))