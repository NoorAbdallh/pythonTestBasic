class item:
    name = ''
    price = 0.0

    def __init__(self,name,price):
        self.price = price
        self.name = name

    def printItem (self):
        print(self.name + '-->' + str(self.price))


    def discount (self,discount):
        self.price = self.price - discount * self.price


class menu:
    def __init__(self):
        self.items = [item('humbergur',1.5),
                      item('rice',1.80),
                      item('tea',1.00)]
    def printMenu(self):
        for item in self.items:
            item.printItem()
    def discountMenu (self,discount):
        if discount>= 0.05 and discount<0.4:
            for item in self.items:
                item.discount(discount)
                item.printItem()
        else:
            print('wrong discount ')

print('**Welcome to our Resturant**')
while(True):
    print('\n************************\n')
    print('input your choice')
    print('1-print menu')
    print('2-input discount')
    m = menu()
    try:
        choice = int(input())
        if (choice == 1):
            m.printMenu()
        elif choice ==2:
            print('input discount between 0.05 and 0.4')
            discount = float(input())
            m.discountMenu(discount)
        else:
            print('wrong input')
    except ValueError:
        print('wrong input')



