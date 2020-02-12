#An Array (python calls it a list)
aryList = ['cherries', 'apples', 'plums', 'bells', 'melons', 'bars']

#print(aryList[0]) picks the first fruit in aryList

'''for i in range(6): #called hardcoding when limiting to 6 instead of unlimited
    print(i, aryList[i])''' 

aryLength = len(aryList) #assigns aryList to variable aryLength
print('Length of array is', aryLength) 

'''for i in range(aryLength):#more flexible than hardcoding, can add and remove more freely
    print(i, aryList[i])'''

for fruit in aryList: #more flexible
    print(fruit)the
