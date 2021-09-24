import random
list1=[]
list2=[]
list3=[]
z=int(input('Введите длину списка'))

def spisok(c):
    for i in range(c):
        list1.append(random.randint(0,100))
        list2.append(random.randint(0,100))
    print(list1)
    print(list2)

    list3=list(set(list1) & set(list2))
    print()
    print('Новый список с повторяющимися элементами', list3)
spisok(z)
