frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == palavras: print('É um palíndromo!')
else: print('Não é um palíndromo!')