import os
import random
os.system ("cls||clear")

# append() - Insere um valor sempre na ultima posição do vetor
# insert() - Insere um valor em qualquer posição do vetor Ex: 0.88, onde zero é a posição e 88 o valor a ser inserido
# pop()    - Deleta uma posição lista
# remove() - Deleta um valor Ex: inserir o valo na lista que deseja remover, se houver dois valores iguais no vetor ele so exclui no primeiro que encontrar
# sum ()   - Soma todos os valores do vetor
# max()    - Procura o maior valor no vetor 
# min()    - Procura o menor valor no vetor 
# choice() - Escolhe uma posição no vetor aleatório 
# sort()   - ordena o vetor, deixa o vetor em ordem 
# set()    - Elimina numeros em uma lista que são repetidos


x=[12,13,45,33,66]
y=[13,21,66,77,88]
uniao = set(x + y)

sortudo= random.choice(x)
x.pop(3)

total = sum(x)
print(uniao)


maiorValor=max(x)
menorValor=min(x)
print(maiorValor)
print(menorValor)