def is_Power(x, y):
   while (x%y == 0):
       x = x / y
   return x == 1
x, y = [int(x) for x in input().split()]
if(is_Power(x, y)):
    print("yes")
else:
    print("no")
