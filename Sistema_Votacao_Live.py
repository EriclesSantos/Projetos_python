#Desenvola um programa em que os colaboradores informe um dos 5 dias da semana (Segunda,Terça,Quarta,Quinta,Sexta)
#para participar da live.VERIFIQUE e EXIBA ao final, qual dia foi escolhido pelos colaboradores.
#OBSERVAÇÂO (VERIFICAR NUMERO  de colaboradores que irão participar da votação para programar a estrutura de repetiçao)
#importante programa validar se a possibildiade de empate.
# Lista dos dias da semana disponíveis para votação

segunda = terca = quarta = quinta = sexta = 0
print("Votação para dia da live!")
num = 0
while num == 0:
        num = int(input("Quantas pessoas vão votar? "))
        if num <= 0:
            print("Digite número Válido!")
            num = 0
for i in range(num):
    print("\n[1]Segunda \n[2]Terca \n[3]Quarta \n[4]Quinta \n[5]Sexta")
    while True:
            voto= int(input(f"Vote de [1-5] Qual o dia da sua prefêrencia: "))
            if voto == 1:
                segunda += 1
                break
            elif voto == 2:
                terca += 1
                break
            elif voto == 3:
                quarta += 1
                break
            elif voto == 4:
                quinta += 1
                break
            elif voto == 5:
                sexta += 1
                break
            else:
                print("Digite uma Opção Válida.")  
print("\nResultado:")
print(f"Segunda: {segunda}")
print(f"Terça: {terca}")
print(f"Quarta: {quarta}")
print(f"Quinta: {quinta}")
print(f"Sexta: {sexta}")
maior = segunda
ganhador = "Segunda"
quantos_empataram = 1 
if terca > maior:
    maior = terca
    ganhador = "Terça"
    quantos_empataram = 1
elif terca == maior:
    quantos_empataram += 1
if quarta > maior:
    maior = quarta
    ganhador = "Quarta"
    quantos_empataram = 1
elif quarta == maior:
    quantos_empataram += 1 
if quinta > maior:
    maior = quinta
    ganhador = "Quinta"
    quantos_empataram = 1
elif quinta == maior:
    quantos_empataram += 1
if sexta > maior:
    maior = sexta
    ganhador = "Sexta"
    quantos_empataram = 1
elif sexta == maior:
    quantos_empataram += 1
if quantos_empataram == 1:
    print(f"\nO dia vencedor foi: {ganhador} com {maior} votos!")
else:
    print("\nHouve um empate entre: ")
    if segunda == maior:
        print("- Segunda")
    if terca == maior:
        print("- Terça")
    if quarta == maior:
        print("- Quarta")
    if quinta == maior:
        print("- Quinta")
    if sexta == maior:
        print("- Sexta")
    print(f"Todos com {maior} votos cada.")