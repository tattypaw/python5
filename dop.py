#задача калькулятор необязательная. Решать только через рекурсию!. Пользоваться встроенными функциями вычисления таких выражений нельзя, если только для проверки вашего алгоритма. на вход подается строка из операторов / * + - и целых чисел. Надо посчитать результат введенного выражения. Например,на входе
#1+9/3*7-4
#на выходе 18

def sum_rec(a, b):
  if b == 0:
    return a
  else:
    a +=1
    b -=1
    return sum_rec(a, b)

def diff_rec(a, b):
  if b==0:
    return a
  else:
    a -=1
    b -=1
    return diff_rec(a, b)

def mult_rec(a, b, mult):
  if b==0:
    return mult
  else:
    mult = sum_rec(mult, a)
    b -=1
    return mult_rec(a, b, mult)

def draw_rec(a,b,n):
  d = diff_rec(a, b)
  if d<=0:
    return n
  else:
    n = n + 1
    return draw_rec(d, b, n)
  return

def NumLeft(s, n):   
  res = ''       
  while s[n-1] in '0123456789' and n > 0 :
    res = s[n-1] + res
    n = n - 1
  return int(res)

def NumRight(s, n):   
  if n == len(s) - 1: res = s[n]
  else:
    res = ''       
    while n < len(s)-1:
      if s[n+1] in '0123456789' :
        res = res + s[n+1]
        n = n + 1
      else:
        if s[n+1] in '*+-/':break
  return int(res)

S = input('Введите арифметическое выражение: ')

#S = '1+9/3*7-4' #Test
F = S


M = S.find('*')            
D = S.find('/') 

while M!=-1 or D !=-1:
  if M != -1 and D != -1:
    if M < D:
      R = NumLeft(F, M)*NumRight(F, M)
      F = F[:(M-len(str(NumLeft(F, M))))] + str(int(R)) + F[M+1+len(str(NumRight(F, M))):]
    else:
      R = NumLeft(F, D)/NumRight(F, D)
      F = F[:(D-len(str(NumLeft(F, D))))] + str(int(R)) + F[D+1+len(str(NumRight(F, D))):]
  else:
    if M == -1:
      R = NumLeft(F, D)/NumRight(F, D)
      F = F[:(D-len(str(NumLeft(F, D))))] + str(int(R)) + F[D+1+len(str(NumRight(F, D))):]
    else:
      R = NumLeft(F, M)*NumRight(F, M)
      F = F[:(M-len(str(NumLeft(F, M))))] + str(int(R)) + F[M+1+len(str(NumRight(F, M))):]
  M = F.find('*')            
  D = F.find('/')


SM = F.find('+') 
DF = F.find('-') 

while SM!=-1 or DF !=-1:
  if SM != -1:
    R = NumLeft(F, SM)+NumRight(F, SM)
    F = F[:(SM-len(str(NumLeft(F, SM))))] + str(int(R)) + F[SM+1+len(str(NumRight(F, SM))):]
  else:
    R = NumLeft(F, DF)-NumRight(F, DF)
    F = F[:(DF-len(str(NumLeft(F, DF))))] + str(int(R)) + F[DF+1+len(str(NumRight(F, DF))):]
  SM = F.find('+') 
  DF = F.find('-') 


print(F)