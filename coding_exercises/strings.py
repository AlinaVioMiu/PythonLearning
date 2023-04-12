# Folosind o singură linie de cod :
# - citește un string de la tastatură (ex: 'alabala portocala');
# - salvează fiecare cuvânt într-o variabilă;
# - printează ambele variabile pentru verificare.
print(input('introduceti un text: ').split())

# Exercițiu:citește de la tastatură un string de dimensiune impară;
# afișează caracterul din mijloc.
text = input('Introduceti un text (doar dimensiunea impara este acceptata): ')
dimensiune_impara = []
for ele in text.split():
    if len(ele) % 2:
        dimensiune_impara.append(ele)
        print('Cuvinte cu dimensiune impara: ' + str(dimensiune_impara))
        print(f'caracterul din mijloc este: {text[len(text) // 2]}')
    else:
        print(f'Textul introdus nu are dimensiune impara. Reincercati.')

# Exercițiu:
# - citește un string de la tastatură (ex: alabala portocala);
# - salvează primul caracter într-o variabilă - indiferent care este el, încearcă
# cu 2 stringuri diferite;
# - capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul
# caracter => alAbAlA portocAla.

string = input("Intoduceti mai multe cuvinte separate printr-un spatiu: ")
prima_litera = string[0].lower()
ultima_litera = string[len(string) - 1].lower()
copy = string[1:len(string) - 1]
print(copy)
copy = copy.replace(prima_litera, prima_litera.upper())
print(copy)
text_modificat = prima_litera + copy + ultima_litera
print(text_modificat)

# Fiind dat un string, sa se afiseze doar consoanele din el
cuvant = 'abecedar'
print(cuvant)
vowels = 'aeiouAEIOU'
result = ''
for i in cuvant:
    if i not in vowels:
        result += i
print(result)

# Conversia unui string de forma "1.234.567,89 Lei" la un float de forma 1234567.89
un_string = "1.234.567,89 Lei"
print(un_string)
un_float = un_string.replace('.', '', ).replace(',', '.').replace('Lei', '')
print(un_float)

# Citește o literă de la tastatură.Verifică și afișează dacă este vocală sau nu.
litera = str(input('Introdu o litera: '))
vocale = 'aeiouAEIOU'
if litera in vocale:
    print(f'{litera} este o vocala')
else:
    print(f'{litera} nu este o vocala')

# Având stringul: 'Coral is either the stupidest animal or the smartest rock'
# ● Citește de la tastatură un int x
# ● Afișează stringul fără ultimele x caractere
# Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
text = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('x = '))
text_modificat = text[0:len(text) - x]
print(text_modificat)
#
# Același string. Declară un string nou care să fie format din primele 5
# caractere + ultimele 5.
text_nou = text[0:5] + text[-5:len(text)]
print(text_nou)
#
# Același string.
# ● Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint:
# este o funcție care te ajuta sa faci asta)
# ● Folosind această variabilă + slicing, afișează tot stringul până la acest
# cuvânt
# ● output: 'Coral is either the stupidest animal or the smartest'
#
cuvant = text.index('rock')
print(cuvant)
text2 = text[0:cuvant]
print(text2)

# 1. Citește de la tastatură un string
# Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
# Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat
string = input('Scrie un cuvant la alegere: ')
prima_litera = string[0].lower()
ultima_litera = string[-1].lower()
string_nou = prima_litera + string[1:len(string) - 1] + ultima_litera
assert string_nou[0] == string_nou[-1]
