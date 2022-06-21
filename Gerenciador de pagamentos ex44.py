print('{:=^40}'.format('Lojas Silva '))
compra = float(input('Preço das compras: R$'))
print(''' Forma de pagamento:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    total = compra - (compra*10/100)
    print('Sua compra de R${:.2f} reais vai sair por R${:.2f} reais no final.'.format(compra, total))

elif opcao == 2:
    total = compra - (compra*5/100)
    print('Sua compra de R${:.2f} reais vai sair por R${:.2f} reais no final.'.format(compra, total))

elif opcao == 3:
    total = compra - (compra/2)
    print('Sua compra sera parcelada em 2x de R${:.2f} reais sem juros'.format(total))
    print('Sua compra de R${:.2f} reais vai sair por 2 parcelas de R${:.2f} reais no final.'.format(compra, total))

elif opcao == 4:
    total = compra + (compra * 20 / 100)
    totalparc = int(input('Quantas parcelas?'))
    parcela = total / totalparc
    print('Sua compra sera parcelada em {}x de R${:.2f} reais COM JUROS'.format(totalparc,parcela))
    print('Sua compra de R${:.2f} reais vai custar R${:.2f} reais no final.'.format(compra, total))

else:
    total = 0
    print('\033[0;31;40m Opção de pagamento inválida. tente novamente!\033[0m')

