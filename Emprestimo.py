print('OLÁ, BEM-VINDO AO SISTEMA DE EMPRÉSTIMO')
valor = float(input('Digite o valor da casa: '))
salario = float(input('Qual o valor do salário do comprador? '))
anos = int (input('Em quantos anos pretende pagar? '))
prestação = valor / (anos * 12)
minimo = salario *30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(valor, anos))
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo CONCEDIDO!')
else:
    print('EMPRÉSTIMO NEGADO!!!')