#problem1
def add(a,b):
    r = a+b
    print(r)
add(12,45)

def substract(a,b):
    r = a-b
    print(r)
substract(2345,1234)

def multiply(a,b):
    r = a*b
    print(r)
multiply(123,2)

def divide(a,b):
    r = a/b
    print(r)
divide(134,24)

#problem2

def word_sum(a):
     c = 0
     for x in a:
         if ('a' <= x <= 'z') or ('A' <= x <= 'Z') or ('а' <= x <= 'я') or ('А' <= x <= 'Я'):
             c += 1
             print(c)
         else:
             pass
a = input('Введите предложение:')
word_sum(a)

#problem3
def dict(a,b):
    a.update(b)
    print(a)
a = {'name':'Ali'}
b = {'age':'16'}
dict(a,b)

#problem4
def pitanie():
    a = open('menu.txt', 'w')
    menuFood = input('Че хавать будешь?\n')
    menuDrink = input("не ичесин чырагым?\n")
    a.write(menuFood)
    a.write(menuDrink)
    a.write(" ")
    a.close()
pitanie()

#problem5
import os
'''def file_open():
    word1 = str(input('Назовите свою директорию: '))
    filee = open(word1, 'a+')
    filee.close()
file_open()'''

#problem6
def first():
    print('Я Главная функция')
    second()

def second():
    print('Я вложенная функия')
first()

#problem7
def dic():
    dict1 = {'name': 1, 'jctor' : 4}
    a = (dict1.keys())
    b = (dict1.values())
    print (a,b)
dic()

#problem8
def prostye_chisla():
	print('Алгоритм нахождения простых чисел')
	a = eval(input('Введите конечное число: '))
	for num in range(a):
		prime = True
		for i in range(2,num):
			if (num%i==0):
				prime = False
		if prime:
			print (num)
prostye_chisla()

#problem9
def func(cars, number):
    print(list(cars))
    print(list(number))


func(['lamba', ('lamborginii')], [13])

#problem10
def fucti():
    a = input('Введите число: ')
    b = int(a)
    c = a * b
    print(c)
    d = len(a)
    f = len(c)
    result = f / d
    print('Всех чисел',a ,'в этом тексте составляет:' , result)
fucti()

#problem11
def problema(name, cash = 5000):
    a = input('Введите свою зарплату: ')
    if a == '':
        print(name, '-', cash )
    else:
        print(name, '-', a)
problema(name = input('whats your name ? : '))

#problem12
from random import *
def random(number):
  	a = []
  	i = 0
  	while i < number:
  		s = randrange(0,1000)
  		if s in a :
  			continue
  		a.append(s)
  		i += 1
  	print(a)
random(number = int(input("Введите число: ")))
