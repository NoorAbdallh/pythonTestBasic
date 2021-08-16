car = '***'
class Car:
    #color = ''
    #engin = 0
    #price = 0.0
    #type = ''
    def __init__(self,c,e,p,t):
        car = ':)'
        self.color=c
        self.engin = e
        self.type=t
        self.price=p
        print(car)

    def printCar(self):
        print('The car is :')
        print(self.type + ' ' + self.color + ' ' + str(self.engin) + ' '+ str(self.price) +'  wow!!!')

car1 = Car('Black','8000',11000,'Audi')
#car1.price = 11000
#car1.engin = 8000
#car1.color = 'Black'
#car1.type = 'Audi'
if car1.color == 'Black':
    car1.printCar()
print(car)
