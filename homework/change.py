import random
list=[]
z=int(input('Введите длину списка'))

def spisok(c):
    for i in range(c):
        list.append(random.randint(0,100))
spisok(z)
print(list)
x=int(input('Введите максимальное число списка'))
for i,n in enumerate (list):
     if n == x:
        list[i] = i
print(list)
