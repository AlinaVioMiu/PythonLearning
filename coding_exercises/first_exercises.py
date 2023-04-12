# T e m a 1 - Setup, Variabile, Tipuri de date

# Declară și initializează câte o variabilă din fiecare din următoarele
# tipuri de variabilă:
# string
mobilier = 'canapea'
# int
varsta_angajat = 50
# float
pret_canapea = 333.5
# bool
disponibitate_canapea = False

# Utilizează funcția type pentru a verifica dacă au tipul de date așteptat.
print(type(mobilier))
print(type(varsta_angajat))
print(type(pret_canapea))
print(type(disponibitate_canapea))

# Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare
# în aceeași variabilă (suprascriere): Verifică tipul acesteia.
pret_canapea = round(333.5)
print(type(pret_canapea))

# Folosește print() și printează în consolă 4 propoziții folosind cele 4 variabile.
# Rezolvă nepotrivirile de tip prin ce modalitate dorești.
print(f'Intentionez sa achizitionez o {mobilier}.')
print(f'Angajatii magazinului cu varsta peste {varsta_angajat} ani primesc un bonus.')
print(f'Pretul canapelei este de : {pret_canapea} lei.')
print(f'Canapeaua este disponibila online? {disponibitate_canapea}')

# Citește de la tastatură: numele; prenumele. Afișează: 'Numele complet are x caractere'.
nume = input('Numele = ')
prenume = input('Prenumele = ')
print(f'Numele complet are', len(nume + prenume), 'caractere.')

# Citește de la tastatură: lungimea; lățimea.
# Afișează: 'Aria dreptunghiului este x'.
lungimea = float(input('Lungimea ='))
latimea = float(input('Latimea ='))
aria_dreptunghi = lungimea * latimea
print(f'Aria dreptunghiului = {aria_dreptunghi}')

# Același string: Verifica dacă acest string conține doar numere.
expresie = 'Coral is either the stupidest animal or the smartest rock'
print(f'Expresia: {expresie}, contine doar numere.')
assert expresie == str(expresie)

print(expresie.isdigit())
print(expresie.isnumeric())

# Verifică și afișează dacă x este număr natural sau nu.
x = 4

if x >= 0:
    print(f'Numarul {x} este natural.')
else:
    print(f'Numarul {x} nu este natural.')
#
# Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.
if x < 0:
    print(f'Numarul {x} este negativ.')
elif x == 0:
    print(f'Numarul {x} este neutru.')
else:
    print(f'Numarul {x} pozitiv.')

# Verifică și afișează dacă x este între -2 și 13.
if x >= -2 and x <= 13:
    print(f'x = {x}')
else:
    print(f'{x} nu este între -2 și 13.')

# Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
y = 4
if (x - y) < 5:
    print(True)
    print(f'{x-y = }')
else:
    print(False)
    print(f'Diferenta dintre {x} si {y} este mai mare sau egala cu 5.')
#
# Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
if x not in range(5, 28):
    print(False, f'\n{x} nu face parte din lista.')
else:
    print(True)

# x și y (int)
# Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai mare.
if x != y:
    if x > y:
        print(f'{x} > {y} \nx este mai mare decat y')
    else:
        print(f'{y} > {x} \ny este mai mare decat x')
else:
    print(f'{x} = {y}')
