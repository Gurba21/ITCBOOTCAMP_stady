#problem0
'''a = {3,10,11,13,31,21,1,10,3,5,6,6}
a.discard(7)
print(a)'''

#problem1
'''a = {"dog", "cat", "mouse", "sheep"}
b = {"cow", "horse", "donkey", "cat", "dog"}
a.intersection_update(b)
print(a)'''

#problem2
'''a = {"cow", "horse", "donkey", "cat", "dog"}
b = {"dog", "cat", "mouse", "sheep"}
print(a.difference(b))'''

#problem3
'''a = {"ali", 'uli', 'baka', 'dosya', 'nurs'}
print(a.pop())'''

#problem4
'''menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
menu.update({'besh_barmak':"130"})
print(menu)
menu["lagman"]=135
print(menu)
del menu['borsh']
print(menu)'''

#problem5
'''menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
#menu.update({'drinks':'Coca-Cola, Sprite, Fanta'})
#print(menu)
menu.update({'drinks':'coca-cola,sprite,fanta'})
print(menu)'''

#problem6
'''a = {'add','update', 'remove','difference','intersection','intersecton_update','clear','discard','pop'}
b = {'clear','get','keys','items','values','update','tuple','set','list','dict'}
a.intersection(b)
print(a)'''

#problem7
'''a={}
b=input(('vedite name:'))
c=input(('vedite password:'))
a[b]=c
print(a)'''

#problem8
'''a=input(('hello','say yours name:'))
b=input(('your jobs:'))
print(a,'good job')'''

#problem9
'''a = {} 
b = input("Введите 10 чисел")
c = input()
d = input()
e = input()
f = input()
j = input()
i = input()
k = input()
l = input()
o = input()
a.update({b : "1 число"}) 
a.update({c : "2 число"}) 
a.update({d : "3 число"})
a.update({e : "4 число"})
a.update({f : "5 число"}) 
a.update({j : "6 число"}) 
a.update({i : "7 число"})
a.update({k : "8 число"}) 
a.update({l : "9 число"}) 
a.update({o : "10 число"}) 
print(a)'''
