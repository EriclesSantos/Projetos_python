#A compra de um veiculo pode ser realizada parcelada.crie um programa que receba o valor de um carro e moestre uma tabela com os seguintes dados:
#PREÇO FINAL, QUANTIDADE DE PARCELAS, VALOR DA PARCELA consideraçoes.
#A) o preço final para compra á vista tem um desconto de 20%
#B)quantidade de parcelas
#  6 /12/18/ 24/ 30/ 36/42 / 48/54/60
# 3%/6%/9%/12%/15%/18%/21%/24%/27%/30%

valor_carro = float(input("Digite o valor do carro R$: "))
avista = valor_carro * 0.80  
parcelas = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
juros = [0.03, 0.06, 0.09, 0.12, 0.15, 0.18, 0.21, 0.24, 0.27, 0.30] 

print(f"\nPreço Final à vista com 20% de desconto R$:{avista:.2f}")
for i in range(10): 
    num_parcelas = parcelas[i]
    taxa_juros = juros[i]
    preco_final = valor_carro * (1 + taxa_juros)  
    valor_parcela = preco_final / num_parcelas
    print(f"O Preço final Parcelado em {num_parcelas}X é de R$ {preco_final:.2f} com parcelas de R$ {valor_parcela:.2f}")

 
    
