texto= input("infome o texto:")
VOGAIS= "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()


for numero in range(0,70,3):
    print(numero)       #usado dessa forma os numeros vao para baixo
    

for numero in range(0,70,3):
    print (numero,end=" " )     #usando dessa forma os numeros seguem em linha


   