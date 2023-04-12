import pytest

from coding_exercises.functions import divizori_numar, numar_prim, dublare_numere_divizibile7, nota_max, \
    perechi_elemente, string_in_l33t


# 1-> given datele probl-initializeaza tot ce e nevoie de input pt a testa
# 2-> when - apelul in librarie
# 3-> then -asserturile care se pot intampla

# - Fiind dat un numar, sa se afiseze divizorii lui.

def test_divizori_numar():
    numar = 87
    dn = divizori_numar(numar)
    assert (1, 3, 29, 87)


# - Fiind dat un numar, sa se afiseze daca este prim sau nu.
def test_numar_prim():
    nr = 3
    np = numar_prim(3)
    assert True


def test_numar_prim2():
    numar_prim(45)
    assert 'Numarul nu este prim'


# # - Fiind data o lista cu numere, sa se dubleze toate numerele divizibile cu 7.
def test_dublare_numere_divizibile_cu_7():
    dublare_numere_divizibile7(3, 4, 7, 21)
    assert [14, 42]


# - Fiind dat un dictionar cu perechi {nume: nota},
# sa se afle cine are cea mai mare nota.
def test_nota_max():
    nota_max(Andrei=7, Maria=10, Ana=8)
    assert 'Maria'


# - Fiind date 2 liste cu elemente, sa se afiseze toate perechile posibile.
def test_perechi_elemente():
    lista1 = [1, 3]
    lista2 = [4, 7]
    perechi_elemente(lista1, lista2)
    assert [(1, 4), (1, 7), (3, 4), (3, 7)]


# Scrieti un algoritm care transforma un string in forma lui L33t. Adica inlocuieste caracterele
# E/e -> 3
# i/I -> 1
# O/o -> 0
# A/a -> 4
# S/s -> 5
# T/t -> 7
# ex: explicatie -> 3xpl1c4t13
def test_string_in_l33t():
    string_in_l33t('explicatie')
    assert '3xpl1c4713'
