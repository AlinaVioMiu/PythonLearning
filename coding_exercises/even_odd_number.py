# # Verifică dacă x este număr par sau impar (x e int).
x = int(input('x = '))
if x % 2 != 0:
    print(f'{x} este numar impar.')
else:
    print(f'{x} este numar par.')

# Având stringul '0123456789'
# ● Afișează doar numerele pare
# ● Afișează doar numerele impare
# (hint: folosește slicing, controlează din pas)
stringul = '0123456789'
stringul_nou = stringul[0:len(stringul):2]
print(stringul_nou)
stringul_nou = stringul[1:len(stringul):2]
print(stringul_nou)