# Scrieti un algoritm care transforma un string in forma lui L33t. Adica inlocuieste caracterele
# E/e -> 3
# i/I -> 1
# O/o -> 0
# A/a -> 4
# S/s -> 5
# T/t -> 7
# ex: explicatie -> 3xpl1c4t13
text = input("Introduceti textul: ")
print(text)
leet = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 'A': '4', 'E': '3', 'I': '1', 'O': '0', 's': '5', 'S': '5', 't': '7', 'T': '7'}

for k, v in leet.items():
    text = text.replace(k, v)
print(text)