print ('-' *30)

print (' ' *3, 'Sequência de Fibonacci')

print ('-' *30)

Valor = int(input('Insira um número: '))

Termo1 = 0

Termo2 = 1

print ('{} → {}'.format(Termo1, Termo2), end='')

Contador = 3

while Contador <= Valor:

   Termo3 = Termo1 + Termo2

   print (' → {}'.format(Termo3), end='')

   Termo1 = Termo2

   Termo2 = Termo3

   Contador += 1

print (' → FIM')