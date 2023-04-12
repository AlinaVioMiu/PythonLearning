import math
import delta as delta
import cmath

# x, y, z - laturile unui triunghi.
# Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
x = 5
y = 6
z = 4
if x == y == z:
    print(f'Triunghiul este echilateral.')
elif x == y or x == z or y == z:
    print(f'Triunghiul este isoscel.')
else:
    print(f'Triunghi oarecare.')

# Fiind dat un numar citit de la tastatura, sa se afiseze jumatatea lui.
numar = int(input("Introduceti numarul: "))
print(f"Jumatatea lui {numar} este {numar / 2}")

# Fiind dat un numar citit de la tastatura, sa se afiseze divizibilitatea lui cu 7.
numar2 = float(input('Introdu un numar: '))
print(f'Numarul ales ({numar2}) este divizibil la 7: {numar2 % 7 == 0}')

# Fiind dat un numar citit de la tastatura, sa se afiseze radicalul lui.
numar3 = float(input('Introdu un numar: '))
print(f'Radicalul numarului {numar3} este {numar3 ** (1 / 2)}')

radical = math.sqrt(numar)
print(f'Radicalul numarului {numar3} este {radical}')

# Fiind data o valoare de imprumut si un numar de luni in cate o variabila,
# sa se afiseze rata lunara luand in calcul dobanda 0% si comision 0%.
valoare_imprumut = float(input('Indicati valoarea de imprumut (lei): '))
numar_luni = int(input('Indicati perioada de rambursare (in luni): '))
rata_lunara = valoare_imprumut / numar_luni
print(
    f'Pentru suma imprumutata in valoare de {valoare_imprumut} lei, pe o perioada de {numar_luni} luni, rata dvs. lunara este de {rata_lunara} lei')

# Fiind date 3 numere citite de la tastatura, sa se afiseze media lor armonica.
q = int(input('Introduceti numarul q: '))
w = int(input('Introduceti numarul w: '))
e = int(input('Introduceti numarul e: '))
media_armonica = 3 * (q * w * e) / (q + w + e)
print(f'Media armonica a nr. {q}, {w} si {e} este {media_armonica}')

# Fiind date 3 numere a, b, c si 3 ponderi p, q, r sa se afiseze media lor ponderata.
# Valorile variabilelor pot fi hardcoded.
a = 10
b = 16
c = 29
p = 2
q = 3
r = 1
media_ponderata = (a * p + b * q + c * r) / (p + q + r)
print(f'Media ponderata a numerelor {a}, {b} si {c} este: {media_ponderata}')

# Fiind date 2 numere a, b, sa se afiseze solutia x ecuatiei de gradul 1:
# #a * x + b = 0
print('a * x + b = 0')
a = int(input("Introduceti numarul a: "))
b = int(input("Introduceti numarul b: "))
if a == 0:
    print('Nicio solutie posibila. ')
elif a != 0:
    x = -b / a
    print(f'{a} * {x} + {b}')
    print('x =', x)
elif b == 0:
    print('x = orice numar este posibil. Solutii infinite. ')

# Fiind date 3 numere a, b, c, sa se afiseze solutiile x1, x2 ale ecuatiei de gradul 2:
# a * x ** 2 + b * x + c = 0.

print('a * x ** 2 + b * x + c = 0')
a = int(input("Introduceti numarul a: "))
b = int(input("Introduceti numarul b: "))
c = int(input("Introduceti numarul c: "))

if a != 0:
    delta = b ** 2 - 4 * a * c
    print(delta)
    if delta < 0:
        print('Nicio solutie posibila. ')
    elif delta == 0:
        x = -b / (2 * a)
        print('O singura solutie posibila. x1 = x2 = ', x)
    else:
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        print('x1 = ', x1)
        print('x2 = ', x2)
else:
    if b == 0:
        print('x = orice numar este posibil. Solutii infinite. ')
    else:
        print('Nicio solutie posibila. ')

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
delta = b ** 2 - 4 * a * c
if delta >= 0:
    x1 = (-b - delta ** (1 / 2)) / (2 * a)
    x2 = (-b + delta ** (1 / 2)) / (2 * a)
else:
    x1 = (-b - cmath.sqrt(delta)) / (2 * a)
    x2 = (-b + cmath.sqrt(delta)) / (2 * a)

print(x1, x2)

# Fiind dat un numar, sa se afiseze 25% din 50% din numarul respectiv.
numar = float(input("Introduceti un numar: "))
jumatate_numar = numar / 2
print(f'25% din 50% din numarul ales este: {jumatate_numar * 0.25}')

# Fiind dat un numar, sa se afiseze divizorii lui.
numar = int(input('Introduceti un numar: '))
for i in range(1, numar + 1):
  if numar % i == 0:
      print(f'Divizorii numarului {numar} sunt: {i} ')

# Sa se calculeze produsul tuturor numerelor pare intre 0 si 50
produs = 0
for num in range(1, 52, 2):
    produs = produs * num
    # print(num)
    # print(f'Produsul este {produs}')
print(f'Produsul este {produs}')

# - Calculul ariei unui cerc, cu raza data dintr-o variabila
raza = float(input('Introdu raza cercului: '))
PI = 3.14
aria = PI * raza * raza
print(f'Aria cercului = {round(aria, 2)}')

# - Reducerea preciziei unui float primit ca parametru la 2 zecimale
a = 3.4536
print(round(a, 2))
print('%.2f' % a)

# # - Produsul tuturor numerelor de la 1 pana la o valoare primita ca parametru
valoare = int(input('Introdu o valoare: '))
produs = 1
for numar in range(1, valoare + 1):
    produs = produs * numar
print(f'Produsul tuturor numerelor de la 1 pana la {valoare} este: {produs}')

# Verifică dacă x are minim 4 cifre (x e int).
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)
x = int(input('x = '))
if x >= 1000:
    print(f'{x} are minim 4 cifre')
else:
    print(f'{x} nu are minim 4 cifre')

# Verifică dacă x are exact 6 cifre.
if x >= 100000 and x <= 999999:
    print(f'{x} are exact 6 cifre')
else:
    print(f'{x} nu are 6 cifre')

#x, y, z - reprezintă unghiurile unui triunghi
# Verifică și afișează dacă triunghiul este valid sau nu.
x = int(input('x = '))
y = int(input('y = '))
z = int(input('z = '))
if (x + y) > z and (x + z) > y and (y + z) > x:
    print(f'Triunghiul este valid.')
else:
    print(f'Triunghiul nu este valid.')

#factorial recursiv
def factorial(numar):
    if numar == 1:
        return 1
    else:
        return numar * factorial(numar - 1)


print(factorial(3))