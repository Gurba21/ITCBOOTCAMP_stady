#problem1
'''def razvorot():
    list_1 = ['ali','age','1','16']
    a = list_1[:2]
    b = list_1[2:]
    a.reverse()
    b.reverse()
    c = a+b
    print(c)
razvorot()'''

#problem2
'''def fib():
    f1 = f2 = 1
    i = 0
    while i < 7:
        f1, f2 = f2, f1 + f2
        i += 1
        print(f1, end = " ")
    print(f2)
fib()'''

#problem3
'''def print_num(x , y):
	while True:
		if operation == '+':
			result = x + y
			print(result)
			break
result=None
a = float(input('a = '))
operation = input('symbol =')
b = float(input('b = '))
print_num(a, b)'''

#problem4
import os
'''def word():
    word1 = str(input('Назовите свою директорию: '))
    filee = open(word1, 'a+')
    filee.close()
word()'''

#problem5
'''import random
def get_nubmer():
    a = ('1','4','5','7','9','0')
    k=[]
    i=0
    while i<6:
        q=random.choice(a)
        k.append(q)
        i+=1
    print(k)
get_nubmer()'''

#BONUS1
'''text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
def string():
    text.title()
print(text.title())'''

#BONUS2
text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
Simple is better than complex.Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!"""
print(text.find("c"))
print(text.find("C"))

for i in text.split():
    if i[0] =="c" or i[0]  == "C":
        print(i)

#BONUS3'
name=input("Name on your bank account? ")
balance=float(input("Your current balance? "))

def printMenu():
    print(name,"Welcome to the Lots of Money Bank")
    print("Enter 'b'(balance), 'd'(deposit), 'w'(withdraw), or'q'(quit)")

def getTransaction():
    transaction=str(input("What would you like to do? "))
    return transaction

def withdraw(bal,amt):
    global balance
    balance=bal-amt
    if balance<0:
        balance=balance-10

def formatCurrency(amt):
    return "$%.2f" %amt

###MAIN PROGRAM###

printMenu()
command=str(getTransaction())

while command!="q":
    if (command=="b"):
        print(name,"Your current balance is",formatCurrency(balance))
        printMenu()
        command=str(getTransaction())
    elif (command=="d"):
        amount=float(input("Amount to deposit? "))
        balance=balance+amount
        printMenu()
        command=str(getTransaction())
    elif (command=="w"):
        amount=float(input("Amount to withdraw? "))
        withdraw(balance,amount)
        printMenu()
        command=str(getTransaction())
    else:
        print("Incorrect command. Please try again.")
        printMenu()
        command=str(getTransaction())

print(name,"Goodbye! See you again soon")
