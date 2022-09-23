'''
 Faça um algoritmo que leia o salário de um
 funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('Qual seu salário? R$'))
novo = salario + (salario * 15 / 100)
print('Se seu salário é R${:.2f}, com aumento de 15% seu salário passa ser R${:.2f}'.format(salario, novo))