# Fiind dat un numar, sa se afiseze daca este prim sau nu.
numar = int(input('Numar = '))
if numar > 1:
    for i in range(2, int(numar/2)+1):
        if (numar % i) == 0:
            print(numar, "nu este un numar prim")
            break
    else:
        print(numar, "este un numar prim")
else:
    print(numar, "nu este un numar prim")
#SAU

n = 45
for i in range(2, n):
    if n % i == 0:
        print(f'Numarul nu este prim.')
        break
else:
    print (f'Numarul este prim.')