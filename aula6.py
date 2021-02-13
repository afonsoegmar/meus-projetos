#Calcula índice de massa corporal
altura = float(input('informe sua altura: '))
peso = float(input('informe seu peso: '))
imc = peso/ altura**2
print(f'seu imc está em {imc:.2f}')
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 < imc < 24.9:
    print('peso normal')
elif 25 < imc < 29.9:
    print('sobrepeso')
elif 30 < imc < 34.9:
    print('obesidade grau 1')
elif 35 < imc < 39.9:
    print('obesidade grau 2')
else:
    print('obesidade grau 3')
