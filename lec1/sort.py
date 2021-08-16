def sort(data):
    size = len(data)
    for i in range(size):
        max = i
        for j in range(i,size):
            if data[max]< data[j]:
                max = j
        temp = data[i]
        data[i]=data[max]
        data[max]=temp
    print (data)

data = [5,4,2,1,7]
sort(data)
sort([100,5,88,90,45,74,63,541])
sort(['a','b','x','z'])
sort(['noor','zainab','xxx']) #decending order