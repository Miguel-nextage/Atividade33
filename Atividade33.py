#mostre-me as seguintes listas derivadas de:
#[0,1,2,3,4,5,6,7,8,,9,10,11,12,13,14,15]
#intervalo de 1 a 9.
#intervalo de 8 a 13.
#números pares.
#números impares.
#todos os multiplos de 2, 3 e 4.
#lista reversa.
#razão enre o intervalo de 10  a 15 pelo intervalo de 3 a 9 em float.

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Intervalos
print(F"Intervalo de 1 a 9 {lista[1:10]}")
print(F"Intervalo de 8 a 13 {lista[8:14]}")

#Pares e Impares
par = [n for n in lista if n % 2 == 0]
print(F"Os pares dessa lista são {par}")

impar = [n for n in lista if n % 2 == 1]
print(F"Os impares dessa lista são {impar}")

#Multiplos de 2, 3 e 4
multiplos_2 = [n for n in lista if n % 2 == 0]
print(F"Os multiplos de 2 dessa lista são {multiplos_2}")

multiplos_3 = [n for n in lista if n % 3 == 0]
print(F"Os multiplos de 3 dessa lista são {multiplos_3}")

multiplos_4 = [n for n in lista if n % 4 == 0]
print(F"Os multiplos de 4 dessa lista são {multiplos_4}")

#Reverter
lista.reverse()
print(f"A lista reversa é {lista}")

#Razao entre intervalos
sum3_9 = []
sum10_15 = []

for i in lista:
    if i >=10 and i <=15:
        sum10_15.append(i)

sum10_15 = sum(sum10_15)


for i in lista:
    if i >=3 and i <=9:
        sum3_9.append(i)

sum3_9 = sum(sum3_9)

razao = (sum3_9 / sum10_15)

print(F"A razao entre os intervalos é {razao}")