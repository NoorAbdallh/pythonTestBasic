n = ['sand','ali','ahmed','sami']
for name in n :
    print (name)
print('we are out the loop :!!')

for i in range (2,20,2):
    print(i)

found = False
for obj in n:
    if obj == 'ali':
        found = True
        print (obj)
        break

print(found)
