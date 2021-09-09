#problem1
a=(lambda a,b,c:(a*b*c))(5,7,4)
print('обьем бассейна',a)

#problem2
a=(lambda a,b:a-b)(365,223)
print('жаны жылга',a)

#problem3
def chet(a):
    if a < 20 and a %2 !=2:
        print(a)
        chet(a+2)
        print(a)
chet(1)

#problem4
def sett(a):
    print(a)
    if a == set():
        return a
    else:
        a.pop()
        return sett(a)
    d={'aaaa', '2df'}
sett(set("b"))

#problem5
import random
def gen(a):
    o = []
    for z in a():
        if z not in o:
            o.append(z)
    print(o)
    print(len(o))
@gen

def neg():
    a1=[]
    i=0
    for i in range(100):
        b=random.randint(10,50)
        a1.append(b)
        return a1

#problem6
def reg(x):
    login = input("Введите логин:")
    password = input("Введите пароль:")
    x(login,password)
@reg
def registratcia(login,password):
  k = 0
  for i in login:
    print(k+ord(i))
    break
  for i in password:
    print(k+ord(i))
    break

#problem7
def mers():
    a=[1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453]
    i = 0
    for i in a:
        sett = (lambda a,b: (b*a))(1.185,i)
        print(sett)
mers()