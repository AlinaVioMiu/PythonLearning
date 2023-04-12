# Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
# Ia numărul ghicit de la utilizator
# Verifică și afișează dacă utilizatorul a ghicit
# Vei avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
# ● Ai ghicit. Felicitări! Ai ales x si zarul a fost y.
import random
num = random.randint(1,6)
dice_roll = int(input('Da cu zarul: '))
print(f'A iesit: {num}')
if dice_roll < num:
    print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {dice_roll} dar a fost {num}.')
elif dice_roll > num:
    print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {dice_roll} dar a fost {num}.')
elif dice_roll == num:
    print(f'Ai ghicit. Felicitări! Ai ales {dice_roll} si zarul a fost {num}.')