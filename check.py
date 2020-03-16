def checkApp():
 rangeValue = int(input("Enter value for range count"))
 for i in range(rangeValue):
    if i % 3  == 0 and i % 5 == 0:
     print(i,' = ab')
    elif i % 3 == 0:
     print(i,' = a')
    elif i % 5 == 0:
     print(i,' = b')
    else: False
 return True

checkApp()
