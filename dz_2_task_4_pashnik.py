# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных
# позициях. Позиции хранятся в файле file.txt в одной строке одно число.

list_of_num = []
list_num_el = []
result = 1

num_n = int(input('write number: '))

for i in range(- num_n, num_n + 1):
    list_of_num.append(i)

with open('file.txt', 'r') as f:
    a = f.read()
    list_num_el = a.split('\n')

for num_el in list_num_el:
    try:
        result *= list_of_num[int(num_el)]
    except IndexError:
        print(f'the file has an invalid index')
        exit(1)
    except ValueError:
        print('the file has an invalid index name')

print(list_of_num)
print('the result of multiplication:', result)
