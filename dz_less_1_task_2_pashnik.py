#  Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

quarter = input('please, write the number of the quarter of the rectangular coordinate system: ')

if quarter == '1' or quarter == 'I':
    print('valid value:\nX = from 0 to +∞\nY = from 0 to +∞')
elif quarter == '2' or quarter == 'II':
    print('valid value:\nX = from  -∞ to 0\nY = from 0 to +∞')
elif quarter == '3' or quarter == 'III':
    print('valid value:\nX = from  -∞ to 0\nY = from  -∞ to 0')
elif quarter == '4' or quarter == 'IV':
    print('valid value:\nX = from 0 to +∞\nY = from  -∞ to 0')
