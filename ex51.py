pt = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
dcm = pt + (10 - 1) *rz
for c in range(pt, dcm, rz):
    print('{} '.format(c), end = ' → ')
print('ACABOU!')