print("chuong trinh dao chuoi! ")
# input: 12345
# process: what do you do ? cai minh muon
# output: 54321


chuoi = input('nhap vao 1 chuoi: ')
chuoi_dao_nguoc = ''
for n in chuoi:
    # print(n, end= ' ')
    chuoi_dao_nguoc = n + chuoi_dao_nguoc

print('input: %s' %chuoi)
print('output: %s' %chuoi_dao_nguoc)