minhalista = [76, 92.3, "oi", True, 4, 76]

#a) Inserir "pitomba" e 76 no final da lista.

minhalista.insert(6, "pitomba")
minhalista.insert(7, 76)
print(minhalista)

#b) Inserir o valor "Cibele" na posição de índice 3.

minhalista.insert(3, "Cibele") 
print(minhalista)

#c) Inserir o valor 99 no início da lista.

minhalista.insert(0, 99)
print(minhalista)

#d) Encontre o índice de "oi".

indice = None
busca = 'oi'

for i, item in enumerate(minhalista):
    if item == busca:
        indice = i
        break
    
if indice is not None:
    print("O indice de", busca, "é", indice)
    
#e) Remover True da lista.

del minhalista[5]

print(minhalista)