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