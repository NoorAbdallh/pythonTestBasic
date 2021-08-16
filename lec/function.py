def likeFruit (fruit):
    print ('I like ' + fruit)

fru = ['apple','banana','cheery','water melon', 'kiwi']
#likeFruit(fru[0])
#likeFruit(fru[1])


#for f in fru :
   # if f == 'kiwi':
       #likeFruit(f)
      # break

def convertUSToJOD(dollar=1):
    total = dollar * 0.71
    return total

def fullName(FName = ' ', MName=' ' ,LName=' '):
    print(FName+' '+MName+' '+LName)

jod = convertUSToJOD()
print(jod)
print (convertUSToJOD(5))

fullName('noor','hani','abdallh')
fullName(LName='Abdallh', FName='Noor')
fullName('Noor')




















