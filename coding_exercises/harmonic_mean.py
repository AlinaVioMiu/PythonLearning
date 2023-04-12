# - Media armonica a oricator valori primite prin parametru
# formula = 3 * a * b * c / (a + b + c)
num = int(input('Scrie cate numere vrei sa folosesti : '))
print(f'Introdu cele {num} numere: ')
valori = []
for i in range(0, num):
    ele = int(input())
    valori.append(ele)
print(valori)
sum = 0
produs = 1
for ele in valori:
    sum = sum + ele
    produs = produs * ele
media_armonica = len(valori) * produs /sum
print(f'Media armonica a numerelor este = {media_armonica}')