x = int(input())
y = int(input())
z = int(input())
n = int(input())

# lista com o loop for
i = [p for p in range(x+1)]
j = [m for m in range(y+1)]
k = [n for n in range(z+1)]

lista = [[q,w,e] for q in i for w in j for e in k]

lista2 = [t for t in lista if sum(t) != n]

print(lista2)