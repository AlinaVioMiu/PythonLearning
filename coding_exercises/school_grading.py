# 10.Transformă și printează notele din sistem românesc în >
# Peste 9 => A
# Peste 8 => B
# Peste 7 => C
# Peste 6 => D
# Peste 4 => E
# 4 sau sub => F

calificativ = float(input('introduceti nota: '))
if calificativ >= 9 and calificativ <= 10:
    print(f'Ati obtinut calificativul A')
elif calificativ >= 8 and calificativ < 9:
    print(f'Ati obtinut calificativul B')
elif calificativ >= 7 and calificativ < 8:
    print(f'Ati obtinut calificativul C')
elif calificativ >= 6 and calificativ < 7:
    print(f'Ati obtinut calificativul D')
elif calificativ > 4 and calificativ < 6:
    print(f'Ati obtinut calificativul E')
elif calificativ <= 4:
    print(f'Ati obtinut calificativul F')
else:
    print('Nu ati introdus o nota valida.')