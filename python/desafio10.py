n = int(input())
arr = map(int, input().split())

lista = sorted(set(arr)) 
print(lista[-2])

#sorted deixa os elementos em ordem crescente 
#set elimina os elementos repetidos
#map implementa uma função em um iterável
#split elimina os espaços por padrão,(pode conter parametros), de uma string