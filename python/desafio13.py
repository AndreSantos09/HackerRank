N = int(input())
lista = []
for _ in range(N):
    l,*args=input().split()
    if l == 'insert':
        lista.insert(int(args[0]),int(args[1]))
    elif l == 'print':
        print(lista)
    elif l == 'append':
        lista.append(int(args[0]))
    elif l == 'sort':
        lista.sort()
    elif l == 'pop':
        lista.pop()
    elif l == 'reverse':
        lista.reverse()
    elif l == 'remove':
        lista.remove(int(args[0]))
            