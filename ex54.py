from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nasc = int(input('\033[1;97m Em que ano a {}° pessoa nasceu: '.format(i)))
    idade = atual - nasc
    if idade >= 18: 
        print('\033[1;92m Essa pessoa tem {} anos de idade, logo ela é maior de idade!'.format(idade))
        totmaior += 1
    else: 
        print('\033[1;91m Essa pessoa tem {} anos de idade, logo ela é menor de idade!'.format(idade))
        totmenor += 1

print('\033[1;95m{} pessoas são maiores de idade e {} são menores de idade'.format(totmaior, totmenor))
