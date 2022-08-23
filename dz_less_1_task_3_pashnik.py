#  Найти расстояние между двумя точками пространства

print('write coordinates first point:')
fp_x = float(input('X = '))
fp_y = float(input('Y = '))
fp_z = float(input('Z = '))

print('write coordinates second point:')
sp_x = float(input('X = '))
sp_y = float(input('Y = '))
sp_z = float(input('Z = '))

length = (((sp_x - fp_x) ** 2) + ((sp_y - fp_y) ** 2) + ((sp_z - fp_z) ** 2)) ** 0.5

print(f'length = {length}')

