#Syntax Error
try:
    eval('x === x')
except SyntaxError:
    print ("A aparut eroarea SyntaxError!")

# - Fiind date 2 liste cu elemente, sa se afiseze toate perechile posibile.
lista1 = [1, 3]
lista2 = [4, 7]
try:
    perechi = []
    for i in lista1:
        for j in lista2:
            perechi.append((i, j))
    print(perechi)
    print(lista1[2])
except IndexError:
    print('A aparut o eroare!')

#8. Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
try:
    dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
    print(dict1.keys(1))
    # print(dict1.keys())
except TypeError:
    print('A aparut o eroare!')


# Fiind dat un numar citit de la tastatura, sa se afiseze jumatatea lui.
try:
    numar = float(input("introduceti un numar: "))
    print(f"Jumatatea lui {numar} este {numar / 2}")
except ValueError:
    print('A aparut o eroare! Ar trebui citita alta valoare de la tastatura! Sunt acceptate doar cifre! ')


#Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
try:
    print(f'Ana a luat nota', dict1['Mihai'])
    print(f'Gigel a luat nota', dict1.get('Gigel'))
    print(f'Dorel a luat nota', dict1.get('Dorel'))
except KeyError:
    print('A aparut o eroare!')