# Você foi procurado por um aluno do curso de produçaõ multimidia do FIAP ON para desenvolver um trabalho em parceria:um serviço em que as 
#pessoas possam usar um estudio profissional para gravar seus videos para o YOUTube com maxima qualidade.O Serviço ganha dinheiro
#por meio de um sistema de assinatura e de um bonus calculado por uma porcentagem sobre o faturamento que o canal do cliente ao longo do ano.
    #sua tarefa e criar um algoritimo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba o valor do bonus
#que o cliente deve pagar a voce. a tabela abaixo mostra a porcentagem de acordo com cada nivel de assinatura:

#basic  30%
#silver 20%
#gold 10%
#platinum 5%

faturamento_anual =float(input("Por favor, Informe o seu faturamento anual: "))
assinatura = input("Por favor, Informe qual e a sua assinatura: \nBasic \nSilver \nGold \nPlatinum: ")
bonus =  0

if assinatura.upper() == "BASIC":
    bonus = faturamento_anual *  0.3
elif assinatura.upper() == "SILVER":
    bonus = faturamento_anual * 0.2
elif assinatura.upper() == "GOLD":
    bonus = faturamento_anual * 0.1
elif assinatura == "PLATINUM":
    bonus = faturamento_anual * 0.05
else:
    
    print("Opção  de assinatura Inválida")

print(f"Para um faturamento anual de {faturamento_anual} o Bônus de {bonus}")