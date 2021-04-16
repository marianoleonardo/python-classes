str1 = input("String 1: ")
str2 = input("String 2: ")

print("Tamanho da String 1: ", len(str1))
print("Tamanho da String 2: ", len(str2))

print("String 1 minúscula: ", str1.lower())
print("String 2 minúscula: ", str2.lower())

print("String 1 em maiúscula: ", str1.upper())
print("String 2 em maiúscula: ", str2.upper())

print("String 1 vem antes na ordem alfabética que a 2? : ", str1 < str2)
print("String 2 vem antes na ordem alfabética que a 1? : ", str2 < str1)

print(str1[0:int((len(str1)/2))] + str2[int((len(str1)/2)):])

str3 = input("String 3 para ser procurada nas duas primeiras strings: ")

print("A string 3 foi encontrada na string 1? : ", str3 in str1)
print("A string 3 foi encontrada na string 2? : ", str3 in str2)
