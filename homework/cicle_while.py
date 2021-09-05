def trio(x,y,z):
    if z == 0:
        print('Введите С не равное 0!!!')
    else:
        while x<y or y == x:
             print(x, '<', y)
             x=x+z
             continue
        print('Bingo!!!', x, '>', y)

a=int(input('Введите число А'))
b=int(input('Введите число B'))
c=int(input('Введите число C'))
trio(a,b,c)
