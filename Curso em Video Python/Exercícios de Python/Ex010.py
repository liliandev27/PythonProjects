'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere: US$1,00 R$5,11 EU$5,03
'''

real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 5.11
euro = real / 5.03
print('Com R${:.2f}, você pode comprar US${:.2f} e EU${:.2f}!'.format(real, dolar, euro))