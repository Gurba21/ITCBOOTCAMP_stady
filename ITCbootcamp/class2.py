#problem1
class Factory:
    def engine(self):
        return  'Двигатель создан'
    def bridge(self):
        return 'Ходовая часть создана'

a=Factory()
print(a.engine())
print(a.bridge())

#problem2
class Toyota(Factory):
    def wheels(self):
        return 'Колеса готовы'
    def windows(self):
        return 'Стекла готовы'

b=Toyota()
print(b.wheels())
print(b.windows())

#problem3
class Zoo:
    def __init__(self,animal_1='Tiger', animal_2='Begemot',animal_3='Lev'):
        self.animal_1 = animal_1
        self.animal_2 = animal_2
        self.animal_3 = animal_3
        self.animal_4  = animal_2, animal_3

a=Zoo()
print(a.animal_1, a.animal_2, a.animal_3,)
a.animal_1 = "Лев"
a.animal_3 = "Змея"
print(a.animal_1, a.animal_2, a.animal_3,"\n",a.animal_4)



#Bonus1
class Student:
    def __init__(self,name, lastname, departament, year_of_entrance):
        self.name = name
        self.lastname=lastname
        self.departament=departament
        self.year_of_entrance = year_of_entrance
    def get_student_info(self):
        print(self.name, self.lastname,', поступил в', self.year_of_entrance, 'году, в учебное заведение:', self.departament)
per = Student('Gurba', 'Ali', 'ITCBootcamp', '2021')
per.get_student_info()


#bonus2
class Airplane:
    def __init__(self,make=' Boing', model = '757', year = '2016', max_speed = '600 km/h', odometer = '10,000 m', is_flying = False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying
    def take_off(self):
        is_flying = True
        land = False
        print('Взлет')
    def fly(self):
        is_flying = True
        land = False
        print('Летит',self.max_speed, self.odometer)
    def land(self):
        is_flying = False
        land = True
        print('Приземление')

a = Airplane()
a.take_off()
b = Airplane()
b.fly()
c = Airplane()
c.land()

#Bonus3
class Car:
     def __init__(self, make, model, year, odometer=0, fuel=70):
         self.make = make
         self.model = model
         self.year = year
         self.odometer = odometer
         self.fuel = fuel

     def drive(self, distance):
         fuel = distance / 10
         if self.fuel >= fuel:
             self.__add_distance(distance)
             self.__subtract_fuel(fuel)
             print('Let’s drive!')
         else:
             print('Need more fuel, please, fill more!')

     def __add_distance(self, distance):
        self.odometer += distance

     def __subtract_fuel(self, fuel):
        self.fuel -= fuel


a = Car('sedan', 'avto', '2020')


#a._Car__add_distance(100)


#a._Car__subtract_fuel(100)


print(a.drive(int('100')))


