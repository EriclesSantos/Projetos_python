#Na oferta de um produto de crédito aos clientes,três informaçoes são muito importantes apresentar ao cliente:VALOR DA DIVIDA, TAXA DE JUROS e o
#NUMERO  de parcelas para pagamento do emprestimo contraido junto á fintech.faca um programa que RECEBE  o Valor de uma DIVIDA e mostre uma
#TABELA  com os seguintes dados:
#VALOR DA DIVIDA, VALOR DO JUROS, QUANTIDADE E VALOR DA PARCELA.
#tabela de quantidade de parcelas e juros.
#quantidade de parcelas                 % de juros sobre o valor inicial da divida
#         1                                                  0
#         3                                                  10
#         6                                                  15
#         9                                                  20
#         12                                                 25

valor_divida =float(input("Valor da divida:"))
quantidade_parcelas = [1, 3 , 6 , 9 ,12]
juros = [0, 0.10, 0.15, 0.20,  0.25]

for i in range(5):
    num_parcelas = quantidade_parcelas[i] 
    taxa = juros[i]
    total_com_juros = valor_divida * (1 + taxa)  
    valor_parcela = total_com_juros / num_parcelas
    print(f"Total R$:{total_com_juros:.2f} Juros {taxa*100:.1f}% {num_parcelas} parcelas no valor de: R$ {valor_parcela:.2f} ")
    