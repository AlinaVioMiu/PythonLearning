# 1. Declară o listă note_muzicale în care să pui do re mi etc până la do
# ● Afișeaz-o.
# ● Inversează ordinea folosind slicing și suprascrie această listă.
# ● Printează varianta actuală (inversată).
# ● Pe această listă aplică o metodă care bănuiești că face același lucru,
# adică să îi inverseze ordinea. Nu trebuie să o suprascrii în acest caz,
# deoarece metoda face asta automat.
# ● Printează varianta actuală a listei. Practic ai ajuns înapoi la varianta
# inițială.
# Concluzii: slicing e temporar, dacă vrei să păstrezi nouă variantă va trebui să
# suprascrii lista sau să o salvezi într-o listă nouă. Metoda găsită de tine face
# suprascrierea automat și permanentizează aceste modificări. Ambele variante
# își găsesc utilitatea în funcție de ce ne dorim în acel moment.
note_muzicale = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI', 'DO']
print(note_muzicale)
note_muzicale2 = note_muzicale[::-1]
print(note_muzicale2)
note_muzicale2.reverse()
print(note_muzicale2)

# 2. De câte ori apare ‘do’?
print(note_muzicale.count('DO'))

# 3.Având 2 liste, [3, 1, 0, 2] și [6, 5, 4]
# Găsește 2 variante să le unești într-o singură listă.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
lista_extinsa = lista1 + lista2
print(lista_extinsa)
lista1.extend(lista2)
print(lista1)

# 4.Sortează și afișează lista generată la exercițiul anterior.
# ● Sortează numărul 0 folosind o funcție.
# ● Afișaza iar lista.
lista1.sort()
print(lista1)
lista1.sort(reverse=True)
print(lista1)

lista1.remove(0)
print(lista1)
lista1.insert(0, 0)
print(lista1)

# 5. Folosind un if verifică lista generată la exercițiul 3 și afișează:
# ● Lista este goală.
# ● Lista nu este goală.
if lista1 == []:
    print(f'Lista este goala.')
else:
    print(f'Lista nu este goala. Lista = {lista1}')

# 6. Folosește o funcție care să șteargă lista de la exercițiul 3.
lista1.clear()

# 7. Copy paste la exercițiul 5. Verifică încă o dată.
# Acum ar trebui să se afișeze că lista e goală.
if lista1 == []:
    print(f'Lista este goala.')
else:
    print(f'Lista nu este goala. Lista = {lista1}')

# - Fiind data o lista cu elemente, sa se afle valoarea maxima.
# Hint: sa mearga si cu numere negative.
lista = [-2, -3, -4, -67, -88]
lista.sort()
print(lista[-1])
# SAU
maxValue = max(lista)
print(maxValue)

# - Fiind data o lista cu numere, sa se dubleze toate numerele divizibile cu 7.
lista_numere = [3, 4, 7, 21]
print(lista_numere)
for numar in lista_numere:
    if numar % 7 == 0:
        print(f'Dublul numarului {numar} divizibil cu 7 = {numar * 2}')

# - Fiind date 2 liste cu elemente, sa se afiseze toate perechile posibile.
lista1 = [1, 3]
lista2 = [4, 7]
perechi = []
for i in lista1:
    for j in lista2:
        perechi.append((i, j))
print(perechi)
