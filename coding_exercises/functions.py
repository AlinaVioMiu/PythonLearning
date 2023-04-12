# Fiind dat un string, sa se afiseze doar consoanele din el.
def consoane_cuvant(cuvant):
    result = ''
    for c in cuvant:
        if c not in 'aeiouAEIOU':
            result += c
    return result


cuvant = 'abecedar'
print(consoane_cuvant(cuvant))


# Fiind dat un numar, sa se afiseze divizorii lui.
def divizori_numar(numar):
    for i in range(1, numar + 1):
        if numar % i == 0:
            pass
            print(i)


print(divizori_numar(87))


# Sa se calculeze produsul tuturor numerelor pare intre 0 si 50
def produsul_numerelor_pare(num):
    produs = 1
    for num in range(2, num + 2, 2):
        produs = produs * num
    return produs


print(produsul_numerelor_pare(87))


# Sa se calculeze media ponderata a 3 variabile a, b, c cu ponderile p1, p2, p3.
def media_ponderata2(a, b, c, p1, q2, r3):
    media_ponderata = (a * p1 + b * q2 + c * r3) / (p1 + q2 + r3)
    return media_ponderata


print(media_ponderata2(2, 3, 4, 1, 2, 3))


# Fiind dat un numar, sa se afiseze daca este prim sau nu.
def numar_prim(n):
    for i in range(2, n):
        if n % i == 0:
            print(f'Numarul nu este prim.')
            break
    else:
        print(f'Numarul este prim.')


print(numar_prim(3))


# Calculul ariei unui cerc, cu raza data dintr-o variabila
def arie_cerc(raza):
    aria = 3.14 * raza * raza
    return round(aria, 2)


print(arie_cerc(3))


# Produsul tuturor numerelor de la 1 pana la o valoare primita ca parametru
def produsul_numerelor(numar):
    produs = 1
    for numar in range(1, numar + 1):
        produs = produs * numar
    return produs


print(produsul_numerelor(4))


# Calculul volumului unei sfere cu raza primita prin parametru
def volum_sfera(raza):
    volum = (4 / 3) * 3.14 * (raza * raza * raza)
    return volum


print(volum_sfera(5))


# Numararea aparitiilor fiecarui caracter dintr-un string primit ca parametru.
# Rezultatul sa fie un dictionar cu forma {"a":1, "b":3, ...}
def count_char(string):
    rezultat = {}
    for char in string:
        if char in rezultat:
            rezultat[char] += 1
        else:
            rezultat[char] = 1
    return rezultat


print(count_char('elefant'))


# Afisarea unui drepunghi umplut cu caracterul '#' in terminal,
# cu latimea si lungimea date ca parametri.
def print_dreptunghi(lungime, latime):
    for i in range(0, latime):
        print('')
        for j in range(0, lungime):
            if (i == 0 or i == latime - 1 or j == 0 or j == lungime - 1):
                print('#', end='')
            else:
                print('#', end='')


print_dreptunghi(10, 4)


# Extra-extra: Generarea unui cerc in terminal, cu raza data de la tastatura.
# Cu dimensiunea bazei luata dintr-o variabila
def print_cerc(r):
    for i in range(0, r):
        for j in range(0, r):
            if ((j == 0) and (i == 0)) or ((j == 0) and (i == r - 1)):
                print(end=" ")
            elif ((j == r - 1) and (i == 0)) or ((j == r - 1)) and (i == r - 1):
                print(end='')
            else:
                print(end='*')
        print()


print_cerc(5)


# Fiind data o lista cu elemente, sa se afle valoarea maxima.
# Hint: sa mearga si cu numere negative.
def afisare_elemente(*args):
    return max(args)


print(afisare_elemente(-3, -45, -6, -1, -4))


# Fiind data o tupla de elemente, sa se calculeze media lor aritmetica.
def media_artimetica(*args):
    return sum(args) / len(args)


print(media_artimetica(1, 2))


# - Fiind data o lista cu numere, sa se dubleze toate numerele divizibile cu 7.
def dublare_numere_divizibile7(*args):
    for i in args:
        if i % 7 == 0:
            print(f'Dublul numarului {i} divizibil cu 7 = {i * 2}')


print(dublare_numere_divizibile7(3, 4, 7, 21))

# Fiind dat un dictionar cu perechi {nume: nota}, sa se afle cine are cea mai mare nota.
catalog_elevi = {'Andrei': 7, 'Maria': 10, 'Ana': 8, 'Ion': 8}
max_nota = max(catalog_elevi, key=catalog_elevi.get)
print(f'Cea mai mare nota o are: {max_nota} => {catalog_elevi.get(max_nota)}')


def nota_max(**kwargs):
    max_nota = max(kwargs, key=kwargs.get)
    return max_nota


print(nota_max(Andrei=7, Maria=10, Ana=8))


# Fiind date 2 liste cu elemente, sa se afiseze toate perechile posibile.
def perechi_elemente(lista1, lista2):
    perechi = []
    for i in lista1:
        for j in lista2:
            perechi.append((i, j))
    return perechi


lista1 = [1, 3]
lista2 = [4, 7]
print(perechi_elemente(lista1, lista2))


# Scrieti un algoritm care transforma un string in forma lui L33t. Adica inlocuieste caracterele
# E/e -> 3
# i/I -> 1
# O/o -> 0
# A/a -> 4
# S/s -> 5
# T/t -> 7
# ex: explicatie -> 3xpl1c4t13
def string_in_l33t(string):
    leet = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'A': '4', 'E': '3', 'I': '1', 'O': '0', 's': '5', 'S': '5',
            't': '7',
            'T': '7'}
    for k, v in leet.items():
        string = string.replace(k, v)
    return string


string = 'explicatie'
print(string_in_l33t(string))
