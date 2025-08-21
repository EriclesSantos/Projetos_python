#Toda vez que um cliente realiza um resgate de uma aplicação financeira, o sistema deve calcular a alíquota de imposto de renda (IR) que deve ser
#aplicada sobre aquele resgate,levando em consideração o numero de dias que o valor permaneceu aplicado, de acordo com a tabela abaixo:
#até 180 dias = alíquota de 22,5% de IR.
# de 181 a 360 dias = alíquota de 20% de IR.
# de 361 a 720 dias = alíquota de 17,5% de IR.
# Acima de 720 dias = alíquota de 15% de IR.
# e oque acontece, por exemplo, com o certificado de deposito Bancário (CDB),uma aplicação de renda fixa comumente oferecida pelas fintechs.Outros
#investimentos em renda fixa, com LCI e LCA, respectivamente, letra de Crédito Imobiliario e letra de credito do agronegocio são isentos de imposto
#de renda.
#Escreva um program que receba o tipo investimento do qual se deseja realizar um resgate:(1 para CDB, 2 para LCI e 3 para LCA),o valor a ser
#resgatado e o numero de dias que esse valor permaneceeu investido e, se for o caso,calcule o valor referente ao imposto de renda.
#observação o programa deve consistir se o investimento fornecido e valido, ou seja 1,2 ou 3.

print("Escolha o tipo de Investimento\n[1]CDB\n[2]LCI\n[3]LCA")
tipo =int(input("Digite o tipo de Invesimento: "))
valor = float(input("Digite o valor a ser resgatado: "))
dia = int(input("Digite o número de dias que o valor permaneceu investido: "))
if tipo not in [1 ,2, 3]:
    print("Tipo de Opção Invalida!")
else:
    if tipo == 1:
        if dia <= 180:
            imposto = 0.225 #22.5%
        elif dia <= 360:
            imposto = 0.20 #20#
        else:
            imposto = 0.15
        valor_imposto = valor * imposto
        valor_liquido = valor - valor_imposto
        print(f"Imposto:R$ {valor_imposto:.2f} Valor líquido :R$ {valor_liquido:.2f}")
    else:
        print("Investimento insento de IR")
        print(f"Valor Líquido:R$ {valor:.2f}")

