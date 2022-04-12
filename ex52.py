tot = 0
num = int(input('Digite um numero: '))
for c in range(1, num + 1):
    if num % c == 0: 
        print('\033[1;92m', end='')
        tot += 1
    else: print('\033[31m', end='')
    print('{} '.format(c), end='')
if tot == 2: print('o numero {} foi divisivelsomente {} vezes e por isso ele é primo'.format(num, tot))
else: print('o numero {} foi divisivel {} vezes e por isso ele não é primo'.format(num, tot))

