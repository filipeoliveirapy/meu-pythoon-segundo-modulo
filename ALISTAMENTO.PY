from datetime import date
nasc = int(input('Qual a ano do seu nascimento: '))
ano = date.today().year
idade = ano - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade, ano))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = ano + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = ano - saldo
    print('Seu alistamento foi em {}'.format(ano))