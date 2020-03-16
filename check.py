def checkApp():
 rangeValueStart = int(input("Enter value for range count"))
 rangeValueStop = int(input("Enter stop value"))
 for i in range(rangeValueStart,rangeValueStop):
    if i % 3  == 0 and i % 5 == 0:
     print(i,' = ab')
    elif i % 3 == 0:
     print(i,' = a')
    elif i % 5 == 0:
     print(i,' = b')
    else: False
 return True

checkApp()
