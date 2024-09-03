numero = int(input('Digite um número: '))

elemento_1 = 0
elemento_2 = 1
fibonacci = [elemento_1, elemento_2,]


while elemento_2 < numero:
    soma = elemento_1 + elemento_2
    fibonacci.append(soma)
    elemento_1 = elemento_2
    elemento_2 = soma


if numero in fibonacci:
    print(f'O número {numero} pertence à sequência de Fibonacci.')
else:
    print(f'O número {numero} NÃO pertence à sequência de Fibonacci.')

print(f'Sequência de Fibonacci: {fibonacci}')

