print ('enter your mark : ')
mark = int (input())

if mark >= 50 :
    print ('pass:)')
else:
    print('fail!')

if mark > 80 :
    print ('excellent')
elif mark >60 :
    print ('good')
elif mark > 50 :
    print ('not bad')
else:
    print ('too bad')