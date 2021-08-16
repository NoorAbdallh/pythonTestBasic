class student:
    firstName = ' '
    lastName = ' '
    avg = 0.0
    SID = ' '
    major = ' '

s = student()
print(type(s))

s.major = 'Engineering'
s.SID = '0202020'
s.avg = 3.9
s.firstName = 'Noor'
s.lastName = 'Abdallh'
print('student name is : ' + s.firstName + ' ' + s.lastName +' student ID :'+s.SID +' their GPA is : ' + str(s.avg) + ' major : ' + s.major)
