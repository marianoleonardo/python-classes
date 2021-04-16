n = int(input("Informe um número inteiro: "))


aux = n
i = n
while i != 1:
    aux = aux * (i - 1)
    i = i -1
print("Fatorial usando while: ", aux)

aux = n
i = 1
for i in range(n-1):
    aux = aux * (i + 1)
print("Fatorial usando for: ", aux)