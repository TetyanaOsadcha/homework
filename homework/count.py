def count():
      a = int(input('Введите число'))
      b=a
      sum = 0
      while a>0:
             i=a % 10
             sum=sum+i
             a=a // 10
      print('Сумма цифр числа',b, '=',sum)

count()
