lista = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    lista.append([name, score])
    
lista2 = sorted(set([x[1] for x in lista]))

for _ in sorted(lista):
    if _ [1] == lista2[1]:
        print(_[0])
    