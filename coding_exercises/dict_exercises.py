# Având dicționarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folosește o funcție că să afișezi Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

# Printează cei 3 elevi și notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o vei lua folosindu-te de cheie
print(f'Ana a luat nota', dict1.get('Ana'))
print(f'Gigel a luat nota', dict1.get('Gigel'))
print(f'Dorel a luat nota', dict1.get('Dorel'))

# Dorel a făcut contestație și a primit 6
# ● Modifică nota lui Dorel în 6
# ● Printează nota după modificare
dict1['Dorel'] = 6
print(f'Dupa contestatie, Dorel a luat nota', dict1.get('Dorel'))

# Gigel se transferă din clasă
# ● Căuta o funcție care să îl șteargă
# ● Vine un coleg nou. Adaugă Ionică, cu nota 9
# ● Printează noii elevi
dict1.pop('Gigel')
dict1.update({'Ionica':print(dict1)})

# - Numararea aparitiilor fiecarui caracter dintr-un string primit ca parametru.
# Rezultatul sa fie un dictionar cu forma {"a":1, "b":3, ...}
text = input('Introdu un text: ')
rezultat = {}
for i in text:
    if i in rezultat:
        rezultat[i] +=1
    else:
        rezultat[i] = 1
print(rezultat)

# - Fiind dat un dictionar cu perechi {nume: nota}, sa se afle cine are cea mai mare nota.
catalog_elevi = {'Andrei': 7, 'Maria': 10, 'Ana': 8, 'Ion': 8}
max_nota = max(catalog_elevi, key=catalog_elevi.get)
print(f'Cea mai mare nota o are: {max_nota} => {catalog_elevi.get(max_nota)}')
