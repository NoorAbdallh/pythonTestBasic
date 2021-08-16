#Noor Resturant
print('***  Welcome to ** Resturant  ***')
class ResturantMenu :
    MainDishMenu = {'humburger': 2.5,
                    'shawermah': 1.75,
                    'flafel' : 1.00
                    }
    DesertMenu = {'apple pie' : 3.00,
                  'mochi' : 0.50,
                  'cake' : 1.00
                  }
def DiscountVlue(x):
    if x >= 0.05 and x <= 0.4 :
        print('The discount is : ' + str(x) + '\n')
    else:
        print('The discount value must be between 0.05 and 0.4  \n')

while(True):
    try:
        print('Enter number 1 to view resurant menu :) ')
        print('Enter number 2 if you have a discount !!! ')
        r = int(input())
        if r == 1:
            customer = ResturantMenu()
            print('The Menu Today is : ')
            print(customer.MainDishMenu)
            print(customer.DesertMenu)
            print('\n')
        elif r == 2:
            print('Enter the discount value : ')
            d = float(input())
            DiscountVlue(d)


    except ValueError:
        print('Enter number 1 or number 2 only !!')

