#voce deve elaborar um algoritmo implementando em python em que o usuario informe quantos alimentos consumiu naquele dia
# e depois possa informar o numero de calorias de cada um dos alimentos. como não estudamos lista nesse cap voce deve se 
#preocupar em armazenar todas as calorias digitadas, mas deve exibir o total de calorias no final.

quantidade_alimentos = int(input(" Informe a quantidade de alimentos que consumiu hoje: "))
total_calorias = 0 

for alimento in range (1, quantidade_alimentos +1 , 1 ):
    caloria = int(input("Informe a quantidade de calorias do {} do alimento: ".format(alimento)))
    total_calorias = total_calorias + caloria 

print("Foram consumidas {} calorias ao longo do dia: ". format(total_calorias))