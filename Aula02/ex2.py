x = float(input("Informe a coordenada X: "))
y = float(input("Informe a coordenada Y: "))

if x == 0 and y == 0:
    print("O ponto p[",x,",",y,"] não se encontra em nenhum quadrante")
elif x > 0 and y > 0:
    print("O ponto p[",x,",",y,"] se encontra no primeiro quadrante")
elif x < 0 and y > 0:
    print("O ponto p[",x,",",y,"] se encontra no segundo quadrante")
elif x < 0 and y < 0:
    print("O ponto p[",x,",",y,"] se encontra no terceiro quadrante")
else:
    print("O ponto p[",x,",",y,"] se encontra no quarto quadrante")