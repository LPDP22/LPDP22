prod1 = float(input("Digite o preco do primeiro produto: "))
prod2 = float(input("Digite o preco do segundo produto: "))
prod3 = float(input("Digite o preco do terceiro produto: "))

if prod1 < prod2 and prod1 < prod3:
    print("O 1º Produto é o mais barato")

elif prod2 < prod1 and prod2 < prod3:
    print("O 2º Produto é o mais barato")

elif prod3 < prod1 and prod3 < prod2:
    print("O 3º Produto é o mais barato")