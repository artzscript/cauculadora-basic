
nome = input(' vamos lá, qual o seu nome? ') 
print('\n Olá {}!! está com problemas em resolver somas dificeis ou até mesmo simples? vou te ajudar nessa!'.format(nome, ))

num1 = int(input('\n Digite um valor: '))
num2 = int(input(' Digite mais um valor: '))

a = num1 + num2
d = num1 / num2
m = num1 * num2 
di = num1 // num2
p = num1 ** num2

print (' a soma é {} a divisão é {:.4f} o produto é {}'.format(a, d, m, ), end=' >>> ')
print ('a divisão inteira é {} e a potência é {}.'.format(di, p, ))
