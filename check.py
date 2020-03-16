print("range from 0-99")
for i in range(100):
   if i % 3  == 0 and i % 5 == 0:
     print(i,' = ab')
   elif i % 3 == 0:
     print(i,' = a')
   elif i % 5 == 0:
     print(i,' = b')
   else: print(i," = no value")
print("range from 2-300")
for i in range(2,300):
       if i % 3 == 0 and i % 5 == 0:
           print(i, ' = ab')
       elif i % 3 == 0:
           print(i, ' = a')
       elif i % 5 == 0:
           print(i, ' = b')
       else:
           print(i, " = no value")
