'''Desenvolva um programa que leia o peso e altura de uma pessoa. Calcule seu IMC e mostre seu ststus de acordo com a tabela abaixo:
Abaixo de 18.5: "Abaixo do peso!"
Entre 18.5 e 25 : "Peso ideal!"
Entre 25 e 30: "Sobrepeso!"
Entre 30 e 40: "Obesidade!"
Acima de 40: "Obesidade mórbida!"'''

peso = float(input('Qual seu peso? (Kg)'))
altura = float(input('Qual sua altura? (m)'))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif 18.5 <= 25:
    print('Você está no Peso Ideal!')
elif 25 <= 30:
    print('Você está com Sobrepeso!')
elif 30 <= 40:
    print('Você está Obeso!')
elif imc > 40:
    print('Você está com Obesidade Mórbida!')
