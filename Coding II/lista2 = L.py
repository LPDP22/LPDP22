L = [14, 15, 16]
lista2 = L
print(L == lista2)
print(L is lista2)
lista2[0] = 1
print(lista2)
print(L)
lista3 = lista2.copy