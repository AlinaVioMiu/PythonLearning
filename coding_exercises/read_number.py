# Sa se defineasca o functie read_number, care sa ceara input
# de la user intr-o bucla si sa incerce conversia spre numar.
# Daca inputul userului nu a fost un numar, cerem un alt input.


def read_number():
    while True:
        user_imput = input("introduceti un numar: ")
        try:
            number = float(user_imput)
            return number
        except ValueError:
            pass


read_number()