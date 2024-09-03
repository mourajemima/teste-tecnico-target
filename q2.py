palavra = input('Digite uma palavra: ')

quantidade_a = 0
existe_a = False

if 'a' in palavra or 'A' in palavra:
    existe_a = True

for letra in palavra:
    if letra.lower() == 'a':
        quantidade_a += 1

if existe_a:
    existe_a = 'verdadeiro'
else:
    existe_a = 'falso'


print(f'É {existe_a} a existência da letra "a" na palavra {palavra}.')
print(f'A letra se repete {quantidade_a} vez/vezes.')



