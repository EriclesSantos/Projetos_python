#Verificar se os batimentos cardiacos por minuto se entram na faixa adequada, Para isso voce deve solicitar que o usuario informe o seu numero de batimentos por minutos (BPM) e a idade.A parti
#apartir disso o script deve verificar e exibir uma mensagem informado se os batimentos do usuario encontra-se DENTRO da faixa
#adequada, ACIMA da faixa adequada ou ABAIXO da faixa Adequada, de acordo com o site tua Saude(
#https://www.tuasaude.com/frequencia-cardiaca/#?~:text=At%C3%A9%202%20anos%20deidade,idoso%3A%2050%20a%2060%20bpm.):

#IDADE BPM

#Ate 2 anos 120 a 140
#De 8 anos até 17 anos 80 a 100
#Adulto sedentário 70 a 80
#Idosos 50 a 60

print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
bpm =int(input("Informe o os BPM: "))
idade= int(input("Digite por favor sua idade:"))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Frequencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
elif idade >= 8 and idade<= 17:
    if bpm >= 80 and bpm <= 100:
        print("Frequencia cardiaca adequada")
    else:
        print("Frequancia cardiaca inadequada")
elif idade >= 18 and idade <= 60:
    if bpm >= 70 and idade <= 80:
        print("Frequencia cardiaca adequada")
    else:
        print("Frequencia inadequada")
elif idade >= 60:
    if bpm >= 50 and bpm <= 60:
        print("Frequencia cardiaca adequada")
    else:
        print("Frequencia cardiaca inadequada")
else:
    print("Não Existe dados para a idade indicada")

