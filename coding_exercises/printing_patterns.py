# - Afisarea unui drepunghi umplut cu caracterul '#' in terminal,
# cu latimea si lungimea date ca parametri.
lungime = int(input('L dreptunghi= '))
latime = int(input('l dreptunghi = '))
for i in range(0, latime):
    print('')
    for j in range(0, lungime):
        if (i == 0 or i == latime - 1 or j == 0 or j == lungime - 1):
            print('#', end='')
        else:
            print('#', end='')

# - Extra-extra: Generarea unui cerc in terminal, cu raza data de la tastatura.
r = int(input('Raza cercului: '))
for i in range(0, r):
    for j in range(0, r):
        if ((j == 0) and (i == 0)) or ((j == 0) and (i == r - 1)):
            print(end=" ")
        elif ((j == r - 1) and (i == 0)) or ((j == r - 1)) and (i == r - 1):
            print(end='')
        else:
            print(end='*')
    print()
