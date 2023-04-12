# Exercițiu:
# - citește un user de la tastatură;
# - citește o parolă;
# - afișează: 'Parola pt user x este ***** și are x caractere';
# - ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să
# afișeze corect.
# eg: parola abc => ***
# parola abcd => ****

user = input("User: ")
password = input("Password: ")
parola_ascunsa = ''
for char in password:
    parola_ascunsa += "*"
print(f"Parola pt user {user} este {parola_ascunsa} si are {len(password)} caractere.")
