# Ne imaginăm o echipă de fotbal pt teren sintetic.
# 3 Schimbări maxime admise:
# ● Declară o Listă cu 5 jucători
# ● Schimbari_efectuate = te joci tu cu valori diferite
# ● Schimbari_max = 3
# Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
# - Efectuează schimbarea
# - Șterge jucătorul scos din listă
# - Adaugă jucătorul intrat
# - Afișază a intrat x, a ieșit y, mai ai z schimbări
# Dacă jucătorul nu e în teren:
# - Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în
# teren’
# - Afișază ‘mai ai z schimbări’

echipa_fotbal = ['George', 'Mihai', 'Andrei', 'Victor', 'Radu']
rezerve = ['Vasile', 'Ion', 'Mircea']
schimbari_max = 3
print(
    f'Bine ai venit in joc! \n')

schimbari_efectuate = 0
while schimbari_efectuate < schimbari_max:
    print(f'Echipa de fotbal = {echipa_fotbal}.')
    jucator = input('Introdu jucatorul care doresti sa iasa din teren: ')
    print(f'Rezervele sunt = {rezerve}.')
    rezerva = input('Introdu o rezerva care sa intre in teren: ')
    if jucator in echipa_fotbal and rezerva in rezerve:
        echipa_fotbal.remove(jucator)
        rezerve.remove(rezerva)
        echipa_fotbal.append(rezerva)
        rezerve.append(jucator)
        schimbari_efectuate += 1
        print(f'A intrat {rezerva}, a ieșit {jucator}.')
    else:
        print(f'Nu se poate efectua schimbarea deoarece jucătorul {jucator} nu e în teren.')
    print(f'Mai ai {schimbari_max - schimbari_efectuate} schimbări')
