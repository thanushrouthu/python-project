print("welcome to the rollercoaster ride")   
height = int(input("whats your height? "))
if height >= 120 :

   print(" you can ride the rollercoaster ")
   age = int(input(" enter your age here "))
   if age > 18 :
    print(" you nedd to pay 12$ ")
   elif age >= 12 <= 18 :   
    print(" you nedd to pay 7$ ")
   if age < 12 :
    print(" you need to pay 5$ ")
else:
   print(" you cannot ride")        