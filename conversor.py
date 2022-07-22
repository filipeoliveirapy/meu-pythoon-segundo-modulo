n = int(input('digite um número: '))
print('- - - - ' * 5 )
print('[1] BINÁRIO')
print('[2] OCTAL')
print('[3] HEXADECIMAL')

pgnt = str(input('DIGITE A OPÇÃO QUE DESEJA CONVERTER: '))
if pgnt =='1':
    print('A conversão de {} para BINÁRIO é {}.'.format(n, bin(n)[2:]))
elif pgnt == '2':
    print('A conversão de {} para OCTAL é {} '.format(n, oct(n)[2:]))
elif pgnt == '3':
    print('A conversão de {} para HEXADECIMAL é {}'.format(n, hex(n)[2:]))
else:
    print('NUMERAÇÃO INVÁLIDA, reinicie a operação!')