#problem1
'''values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
a1 = []
for x in values:
	try:
		set(x)
		a1.append(True)
	except TypeError :
		a1.append(False)
	print(a1)
	print(all(a1)'''

#problem2
'''b = set()
for i in range(5):
	a=input("введи число")
	b.add(a)
print(min(b))
print(b)'''


#problem3
'''try:
	a = input("введите фунцию python:")
	eval(a)
except:
	print("ошибка")'''

#problem4
s = int(input("Введите сумму Кредита (не меньше 50 000!!!) :  "))
while s < 50000:
	p = 3.47
	a = s * (p / 100)
print("Сумма переплаты",round(a,2))
print("общая сумма оплаты :",s+a)
