#  Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У

print('please, write coordinates X and Y')
x = float(input('X: '))
y = float(input('Y: '))

if x == 0:
    print('the point lies on the Y axis')
elif y == 0:
    print('the point lies on the X axis')
elif y > 0:
    if x > 0:
        print('the point lies in the I quarter')
    else:
        print('the point lies in the II quarter')
elif y < 0:
    if x > 0:
        print('the point lies in the IV quarter')
    else:
        print('the point lies in the III quarter')
