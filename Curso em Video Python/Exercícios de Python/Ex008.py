'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

m = float(input('Uma distancia em metros: '))

mm = m * 1000

cm = m * 100

dm = m * 10

dam = m / 10

hm = m / 100

km = m / 1000

print('A media  de  {}m coresponde a \n{:.0f}km \n{:.0f}hm \n{:.0f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m, km, hm, dam, dm, cm, mm))