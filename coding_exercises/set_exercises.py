# zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
# weekend = {'sâmbăta', 'duminică'}
# ● Adaugă în zilele_sapt ‘luni’ ● Afișează zile_sapt
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
zile_sapt2 = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică', 'luni'}
print(zile_sapt2)

# 2.Folosește un if și verifică dacă:
# ● Weekend este un subset al zilelor din săptămânii.
# ● Weekend nu este un subset al zilelor din săptămânii.
if weekend.intersection(zile_sapt) == weekend:
    print('Weekend este un subset al zilelor săptămânii.')
else:
    print('Weekend nu este un subset al zilelor din săptămânii.')
# SAU
print(weekend.issubset(zile_sapt))

# 3. Afișează diferențele dintre aceste 2 seturi.
print(zile_sapt.difference(weekend))
# SAU
print(zile_sapt - weekend)

# 4. Afișează intersecția elementelor din aceste 2 seturi.
print(zile_sapt.intersection(weekend))
