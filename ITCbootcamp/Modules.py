#problem1
print("я функция из my_module.py")

#problem2
import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
print(random.sample(names,4))

#problem3
import os
print(os.name)

#problem4
a=input()
import sys
sys.stderr.write(a)
print(sys.argv)


#problem5
import subprocess
subprocess.call("mdkir i_am_a_python", shell=True)
subprocess.call("ls", shell=True)


#problem6
import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
team_1=random.sample(names,4)
team_2=random.sample(names,4)
team_3=random.sample(names,4)
team_4=random.sample(names,4)
#print(team_1)
#print(team_2)
#print(team_3)
#print(team_4)
if __name__ == "__main__":
    pass

#problem7
import sys
a=input()
sys.stderr.write(a)
#print(sys.argv)

#problem8
from random import *
from string import *
i = int(input("Введите число:"))
passwodr = ""
for i in range (0,1):
    passwodr += choice(ascii_letters)
#print("ваш пароль:", passwodr)

#problem9
a = input("Выберите\nКамень 1\nНожницы 2\nБумага 3\n Ваш выбор : ")
a1 = ["Камень","Бумага","Ножницы"]
if a == "1":
   i = choice(a1)
   if i == "Камень":
#     print("Компютер выбрал ",i," Ничья")
   if i == "Бумага":
 #    print("Компютер выбрал ",i, " Вы Победили!!!" )
   elif i == 'Ножницы':
  #   print("Компютер выбрал ",i,'Вы ПРОИГРАЛИ!!!')
if a == "2":
   i = choice(a1)
   if i == "Камень":
   #  print("Компютер выбрал ",i," Вы ПРОИГРАЛИ!!!")
   if i == "Бумага":
    # print("Компютер выбрал ",i, " Вы Победили!!!" )
   elif i == 'Ножницы':
     #print("Компютер выбрал ",i,' Ничья')
if a == "3":
   i = choice(a1)
   if i == "Камень":
     #print("Компютер выбрал ",i," Вы Победили!!!")
   if i == "Бумага":
     #print("Компютер выбрал ",i, " Ничья" )
   elif i == 'Ножницы':
     #print("Компютер выбрал ",i,'Вы ПРОИГРАЛИ!!!')

